from rest_framework import serializers

from tgdjango.app.models import Message, Profile, MessageResponse, Response


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('telegram_id', 'profile_name', 'avatar_url')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message_id', 'command', 'text', 'from_user', 'created_at')

    from_user = ProfileSerializer(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('message_id', 'text', 'photo_url', 'created_at')


class MessageResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageResponse
        fields = ('message', 'response')

    message = MessageSerializer(read_only=True)
    response = ResponseSerializer(read_only=True)


class StatisticsMessageResponseSerializer(serializers.Serializer):
    date = serializers.DateField()
    commands = serializers.DictField()
