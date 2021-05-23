from i_job.service import raffle
from i_service.celery import app
import logging


logger = logging.getLogger(__name__)

@app.task(max_retries=5, soft_time_limit = 1200, priority=3)
def raffle_task(media_link, winners_count):
    raffle(media_link, winners_count)
