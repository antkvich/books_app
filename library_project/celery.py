from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from .settings import TASK_INTERVAL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')

app = Celery('library_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'send-email-every-x-minutes': {
        'task': 'books.tasks.send_email_task',
        'schedule': int(TASK_INTERVAL) * 60,
    },
}