from django.db import models


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True,
        blank=True,
    )
