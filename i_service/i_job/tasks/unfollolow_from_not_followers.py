
from celery.exceptions import SoftTimeLimitExceeded, MaxRetriesExceededError
import logging
import time
from random import randint

from i_service.celery import app
from i_accounts.models import Account
from i_job.service import InstaClient

logger = logging.getLogger(__name__)

@app.task(max_retries=5, soft_time_limit = 1200, priority=3)
def unfollow_from_not_followers(login):
    """Отписка от неподписанных"""
    try:
        account = Account.objects.get(login=login)
        client = InstaClient(account.login, account.password)
        time.sleep(randint(1, 3))

        if not account.instagram_id:
            user_id = client.get_user_id()
            account.update(instagram_id=user_id)
            time.sleep(randint(1, 5))

        balance = account.user.balance
        followings = client.get_self_followings(account.instagram_id)
        time.sleep(randint(1, 4))
        followers = client.get_user_followers(account.instagram_id)
        time.sleep(randint(1, 4))

        accounts_ids = list(set(idFollowings) - set(idFollowers))

        for account_id in account_ids:
            if client.unfollow(account_id):
                balance-=2
                account.user.update(balance=balance)
                time.sleep(randint(1, 4))
        num_retries = test.request.retries
        seconds_to_wait = 2.0 ** num_retries
        raise test.retry(countdown=seconds_to_wait)

    except MaxRetriesExceededError:
        logger.error("MaxRetriesExceededError")
        return None

    except SoftTimeLimitExceeded:

        logger.error("SoftTimeLimitExceeded")
        return None
