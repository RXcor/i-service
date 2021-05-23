import random
import logging

from i_accounts.models import Account
from InstagramAPI import InstagramAPI


logger = logging.getLogger(__name__)

def set_account_for_public_use():
    accounts = list(Account.objects.filter(public = True))
    random.shuffle(accounts)
    for account in accounts:
        logger.warning(f'LAST SESSION DATA {account.last_session_data()}')
        client = InstagramAPI(**account.last_session_data())
        #client.setProxy(proxy=proxy)
        logger.debug(f'CLIENT CREATED {client}')
        # Проверка актуальности сесси
        if account.isLoggedIn:
            client.getSelfUsernameInfo()
            if client.isLoggedIn:
                logger.debug(f"Client {account.username} is isLoggedIn")
            else:
                logger.debug(f"Client {account.username} is not isLoggedIn")
                account.isLoggedIn = False
                account.save()
        # Вход при необходимости и обновление данных сессии
        logger.debug(f'ACCOUNT LOGIN: {account.isLoggedIn}')
        if not account.isLoggedIn:
            logger.debug(f'CLIENT IS NOT LOGGED IN')
            if client.login():
                logger.error(f'device_id: {client.device_id}, username_id: {client.username_id}, uuid: {client.uuid}, isLoggedIn: {client.isLoggedIn}, client.token: {client.token}, client.sessionid: {client.sessionid}')
                account.device_id = client.device_id
                account.username_id = client.username_id
                account.uuid = client.uuid
                account.isLoggedIn = client.isLoggedIn
                account.token = client.token
                account.sessionid = client.sessionid
                account.save()
            else:
                continue
        #Если сессия актуальна или удалось залогиниться
        #Возвращаем аккаунт
        #Иначе дальше перебираем наши публичные аккаунты
        if account.isLoggedIn:
            return account
        else:
            continue
    # Если перебор закончился и ничего не вернули сообщение в лог
    logger.error('PUBLIC ACCOUNTS IS BLOCKED')
    return None
