# Generated by Django 4.2.3 on 2023-07-28 10:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_messageresponse_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='command',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator('^/[a-zA-Z0-9_]$')], verbose_name='Команда'),
        ),
    ]
