from django_filters import rest_framework as django_filters

from .models import MessageResponse


class MessageResponseFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(field_name='message__from_user__telegram_id')

    class Meta:
        model = MessageResponse
        fields = ('user',)
