import logging
import random
import time
import json
from datetime import datetime


from InstagramAPI import InstagramAPI
from .set_acc_for_pub import set_account_for_public_use
from .get_all_comments import get_all_comments

from i_job.models import Job


logger = logging.getLogger(__name__)

def raffle(media_link, winner_count: int=1):
    job_instance = Job.objects.filter(data=media_link).last()
    logger.warning(media_link)
    logger.warning(winner_count)

    #Создание подключения к апи
    account = set_account_for_public_use()
    logger.debug(f'ACCOUNT {account}')
    if account is None:
        return None
    else:
        client = InstagramAPI(**account.last_session_data())
        #Прогресс
        job_instance.progress=10
        job_instance.save()
    time.sleep(random.uniform(2, 10))
    #Получение media_id
    client.getMediaId(media_link)
    #Прогресс
    job_instance.progress=20
    job_instance.save()

    media_id = client.LastJson['media_id']

    logger.debug(f'MEDIA ID: {media_id}')
    #Получить все комментарии
    if media_id is not None:
        all_comments = get_all_comments(client, media_id)
    else:
        return None
    #Прогресс
    job_instance.progress=70
    job_instance.save()
    #Применение фильтров к комментариям и аккаунтам
    filtrated_comments = all_comments
    #Случайный выбор победивших
    vinners_comments = random.sample(filtrated_comments, winner_count)
    obj_vinners_comments = {'vinners_comments': vinners_comments}
    j_vinners_comments = obj_vinners_comments

    job_instance.progress = 100
    job_instance.save()

    job_instance.result = j_vinners_comments
    job_instance.is_complete = True
    job_instance.completed = datetime.now()
    job_instance.save()

    return vinners_comments
