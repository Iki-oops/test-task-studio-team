from django.core.validators import RegexValidator
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
    avatar_url = models.CharField(
        'Аватар', max_length=80, default='https://i.ibb.co/y68FLSn/anonymous.png'
    )
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.profile_name

    @property
    def profile_name(self):
        if not self.username:
            return f'{self.first_name} {self.last_name}'
        return self.username


class Command(models.Model):
    class Meta:
        verbose_name_plural = 'Команды'
        verbose_name = 'Команда'
        ordering = ('id',)

    command = models.CharField(
        'Команда',
        max_length=30,
        validators=[RegexValidator(r'^/[a-zA-Z0-9_]+$')],
    )
    text = models.TextField()


class Message(TimeBasedModel):
    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ('-created_at', '-updated_at')

    message_id = models.BigIntegerField('Id сообщения', primary_key=True)
    command = models.CharField(
        'Команда',
        max_length=30,
        validators=[RegexValidator(r'^/[a-zA-Z0-9_]+$')],
        null=True,
        blank=True,
    )
    text = models.TextField('Текст')
    from_user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='messages'
    )

    def __str__(self):
        return str(self.message_id)


class Response(TimeBasedModel):
    class Meta:
        verbose_name_plural = 'Ответы бота'
        verbose_name = 'Ответ бота'
        ordering = ('-created_at', '-updated_at')

    message_id = models.BigIntegerField('Id сообщения', primary_key=True)
    text = models.TextField('Текст')
    photo_url = models.CharField(
        'Ссылка на изображение', max_length=150, null=True, blank=True
    )

    def __str__(self):
        return str(self.message_id)


class MessageResponse(TimeBasedModel):
    class Meta:
        verbose_name_plural = 'Сообщении - ответы'
        verbose_name = 'Сообщение - ответ'
        ordering = ('-created_at', '-updated_at')

    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    response = models.OneToOneField(
        Response, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f'{self.message} - {self.response}'
