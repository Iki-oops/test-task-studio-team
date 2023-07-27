from django.db import models

from .abstracts import TimeBasedModel


class Profile(TimeBasedModel):
    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'
        ordering = ('-created_at', '-updated_at')

    telegram_id = models.BigIntegerField('Телеграм id', primary_key=True)
    first_name = models.CharField('Имя', max_length=70, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=70, null=True, blank=True)
    username = models.CharField(
        'Псевдоним', max_length=70, unique=True, null=True, blank=True
    )

    def __str__(self):
        return self.profile_name

    @property
    def profile_name(self):
        if not self.username:
            return f'{self.first_name} {self.last_name}'
        return self.username


class Message(TimeBasedModel):
    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ('-created_at', '-updated_at')

    message_id = models.BigIntegerField('Id сообщения', primary_key=True)
    text = models.TextField('Текст')
    from_user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='messages'
    )

    def __str__(self):
        return self.text


class BotResponse(TimeBasedModel):
    class Meta:
        verbose_name_plural = 'Ответы бота'
        verbose_name = 'Ответ бота'
        ordering = ('-created_at', '-updated_at')

    message_id = models.BigIntegerField('Id сообщения', primary_key=True)
    response = models.TextField('Текст')
    from_command = models.OneToOneField(
        Message, on_delete=models.CASCADE, verbose_name='Команда'
    )

    def __str__(self):
        return str(self.message_id)
