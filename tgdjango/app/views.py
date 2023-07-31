from datetime import datetime, timedelta

from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from tgdjango.app.filters import MessageResponseFilter
from tgdjango.app.models import MessageResponse, Profile, Message
from tgdjango.app.serializers import (
    MessageResponseSerializer,
    ProfileSerializer, StatisticsMessageResponseSerializer,
)


class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MessageResponseViewSet(ReadOnlyModelViewSet):
    queryset = MessageResponse.objects.all()
    serializer_class = MessageResponseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MessageResponseFilter

    @action(methods=['GET'], detail=False)
    def statistics(self, request):
        last_week = datetime.now() - timedelta(days=7)
        popular_command = Message.objects.all()\
            .values('command')\
            .annotate(count=Count('command'))\
            .order_by('-count')\
            .first()

        data = {
            'new_users': Profile.objects.filter(created_at__gte=last_week).count(),
            'active_dialogues': Profile.objects.all().count(),
            'queries': Message.objects.filter(created_at__gte=last_week).count(),
            'popular_command': popular_command.get('command', 0),
        }

        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='detail-statistics')
    def detail_statistics(self, request):
        last_week = datetime.now() - timedelta(days=7)
        messages = Message.objects.filter(updated_at__gte=last_week)\
            .values('created_at', 'command')

        data = []
        for message in messages:
            date = message['created_at'].strftime('%d.%m.%Y')
            command = message['command']

            obj = next((item for item in data if item['date'] == date), None)
            if obj:
                if obj['commands'].get(command):
                    obj['commands'][command] += 1
                else:
                    obj['commands'][command] = 1
            else:
                data.append({'date': date, 'commands': {command: 1}})

        serializer = StatisticsMessageResponseSerializer(data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def commands(self, request):
        commands = Message.objects.order_by('command').values_list('command', flat=True).distinct('command')
        return Response(data=list(commands))
