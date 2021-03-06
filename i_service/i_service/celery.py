import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'i_service.settings')

app = Celery('i_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_transport_options = {
    'queue_order_strategy': 'priority',
    'priority_steps':[0, 1, 2, 3]
}
app.autodiscover_tasks()
app.conf.timezone = 'UTC'

app.conf.beat_schedule = {}
