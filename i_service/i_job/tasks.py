#Для воркера -Ofair

from i_service.celery import app
from celery.exceptions import SoftTimeLimitExceeded, MaxRetriesExceededError
import logging
import time

logger = logging.getLogger(__name__)


@app.task(max_retries=5, soft_time_limit = 10, priority=1)
def test(device_token, message, data=None):

    try:
        time.sleep(2)
        num_retries = test.request.retries
        seconds_to_wait = 2.0 ** num_retries
        raise test.retry(countdown=seconds_to_wait)

    except MaxRetriesExceededError:
        logger.error("MaxRetriesExceededError")
        return None

    except SoftTimeLimitExceeded:
        logger.error("SoftTimeLimitExceeded")
        return None
