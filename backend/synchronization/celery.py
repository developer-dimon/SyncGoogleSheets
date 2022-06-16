import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SyncGoogleSheets.settings')

app = Celery('synchronization')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_orders': {
        'task': 'synchronization.tasks.periodic_update_orders',
        'schedule': crontab(minute=settings.CELERY_UPDATE_ORDERS_SCHEDULE)
    }
}
