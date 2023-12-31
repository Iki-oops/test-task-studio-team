# Generated by Django 4.2.3 on 2023-07-30 09:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_message_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='message',
            name='command',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator('^/[a-zA-Z0-9_]+$')], verbose_name='Команда'),
        ),
    ]
