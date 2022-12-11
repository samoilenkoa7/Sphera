import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sphera.settings')

app = Celery('sphera')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parse_every_30_minutes': {
        'task': 'main.tasks.parse_news_website',
        'schedule': crontab(minute='*/30')
    }
}
