import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamers_pool.settings')
 
app = Celery('gamers_pool')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'beat_weekly_send_news': {
        'task': 'Models.tasks.weekly_send_news',
        'schedule': crontab (hour = 8, minute=0, day_of_week='mon'),
        'args':(),
    },
}

