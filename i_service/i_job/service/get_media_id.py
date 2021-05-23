import requests
import random
import time
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def get_media_id(url):
    logger.warning(f'URL: {url}')

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    #парсинг страницы
    soup = BeautifulSoup (resp.text, 'html.parser')
    #проверка содержимого метатегов
    string_with_id = None
    media_id = None
    for m in soup.find_all('meta'):
        try:
            if 'media?id' in m['content']:
                string_with_id = m['content']
        except KeyError:
            pass
    if string_with_id is not None:
        #'instagram://media?id=1882074346258085831'
        media_id = string_with_id.split('=')[1]
        return media_id
    else:
        logger.warning('string_with_id NOT FOUND')
        return None
