from django.contrib import admin

from .models import Profile, Message, BotResponse


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'first_name', 'last_name', 'username')
    search_fields = ('username', 'first_name', 'last_name',)
    empty_value_display = '--empty--'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'text', 'from_user', 'created_at')
    list_filter = ('from_user', 'text',)
    empty_value_display = '--empty--'


@admin.register(BotResponse)
class BotResponseAdmin(admin.ModelAdmin):
    list_display = (
        'message_id', 'response', 'from_command', 'created_at', 'updated_at'
    )
    list_filter = ('from_command',)
    empty_value_display = '--empty--'
