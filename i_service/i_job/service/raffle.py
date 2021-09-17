import logging
import random
import time

from .proxy import Proxy
from datetime import datetime


from InstagramAPI import InstagramAPI
from .set_acc_for_pub import set_account_for_public_use
from .get_all_comments import get_all_comments
from i_service.env import env
from i_job.models import Job



logger = logging.getLogger(__name__)

def raffle(media_link, **kwargs):
    #Розыгрыш
    winners_count = kwargs.get('winners_count', 1)
    job_instance = Job.objects.filter(data__url=media_link).last()

    #Создание подключения к апи
    account = set_account_for_public_use()
    logger.debug(f'ACCOUNT {account}')
    if account is None:
        return None
    else:
        client = InstagramAPI(**account.last_session_data())
        if env('PROXY_FOR_INSTAGRAM') is not None \
            and len(env('PROXY_FOR_INSTAGRAM')) > 0:
            client.setProxy(proxy=env('PROXY_FOR_INSTAGRAM'))
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
    job_instance.progress=40
    job_instance.save()

    #Применение фильтров к комментариям и аккаунтам без запросов к API
    filtrated_without_api = []

    #Оставить только по одному комментарию каждого пользователя
    us_set = { item['user_id'] for item in all_comments }
    for us in us_set:
        unque_comment = next(
            item for item in all_comments if item['user_id'] == us)
        filtrated_without_api.append(unque_comment)

    winners_comments = []
    while len(winners_comments) < winners_count:
        #Генерация индексов победителей
        indexes = random.sample(
            range(0, len(filtrated_without_api)-1),
            winners_count - len(winners_comments))
        #Вырезка из отобранных комментариев
        checking_comments = [filtrated_without_api.pop(i) for i in indexes]
        #Применение фильтров к комментариям и аккаунтам с доп запросами к API
        filtrated_with_api = checking_comments
        winners_comments += filtrated_with_api

    obj_winners_comments = {'winners_comments': winners_comments}
    j_winners_comments = obj_winners_comments

    job_instance.progress = 95
    job_instance.save()

    job_instance.result = j_winners_comments
    job_instance.save()
    #Замена картинок
    Proxy(job_instance.id).replace_urls()
    job_instance = Job.objects.get(id = job_instance.id)
    job_instance.progress = 100
    job_instance.is_complete = True
    job_instance.completed = datetime.now()
    job_instance.save()


    return winners_comments
