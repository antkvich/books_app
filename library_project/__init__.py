from __future__ import absolute_import, unicode_literals

# Импорт Celery
from .celery import app as celery_app

# Объявляем celery как часть публичного API
__all__ = ('celery_app',)
