import os

import django

os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'tgdjango.tgdjango.settings',
)
os.environ.update(
    {
        'DJANGO_ALLOW_ASYNC_UNSAFE': 'true',
    }
)

django.setup()
