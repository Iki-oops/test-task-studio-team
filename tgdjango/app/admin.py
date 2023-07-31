from django.contrib import admin

from .models import Profile, Message, Response, MessageResponse


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'first_name', 'last_name', 'username', 'is_admin',)
    search_fields = ('username', 'first_name', 'last_name', 'is_admin',)
    empty_value_display = '--empty--'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'command', 'text', 'from_user', 'created_at', 'updated_at')
    list_filter = ('from_user', 'text',)
    empty_value_display = '--empty--'


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'message_id', 'text', 'photo_url', 'created_at', 'updated_at'
    )
    empty_value_display = '--empty--'


@admin.register(MessageResponse)
class MessageResponse(admin.ModelAdmin):
    list_display = ('message', 'response')
    empty_value_display = '--empty--'
