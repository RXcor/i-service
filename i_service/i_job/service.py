from InstagramAPI import InstagramAPI
import requests
import sys
import json
import random
import time
import logging

logger = logging.getLogger(__name__)

class NotLogin(Exception):
    def __init__(self, text):
        self.txt = text


class InstaClient:
    def __init__(
        self,
        username:str='',
        password:str='',
        proxy:str='',
    ):
        self.username = username
        self.client = InstagramAPI(username=username, password=password)
        self.username_id = ''
        self.ready = True

        if len(proxy):
            self.client.setProxy(proxy=proxy)

        if self.client.login():
            self.username_id = self.client.LastJson["logged_in_user"]["pk"]
        else:
            logger.error(f'ОШИБКА АВТОРИЗАЦИИ. USERNAME: {self.username}')
            self.ready = False
            raise NotLogin('Пользователь не авторизован')

    def get_user_id(self, username:str=''):
        """Получить id пользователя"""
        if len(username)==0:
            s_username = self.username
        else:
            s_username = username

        self.client.searchUsername(s_username)
        user_id = self.client.LastJson['user']['pk']
        return user_id

    def get_user_info(self, user_id):
        """Получить информацию о пользователе или о себе"""
        if not user_id:
            r_user_id = self.username_id
        else:
            r_user_id = user_id
        info = self.client.getUsernameInfo(r_user_id)
        return info

    def get_self_followings(self, user_id):
        """Получить список id аккаунтов, на которые подписаны"""
        idFollowings = []
        idFollowings = self.client.getTotalFollowings(user_id)
        return idFollowings

    def get_user_followers(self, user_id):
        """Получить список id аккаунтов, которые подписаны на наш"""
        idFollowers = []
        idFollowers = self.client.getTotalFollowers(user_id)
        return idFollowers

    def unfollow(self, user_id):
        """Отписка"""
        self.client.unfollow.(user_id)

    def follow(self, user_id):
        """Подписка"""
        self.client.follow(user_id)

    def like(self, media_id):
        """Лайк"""
        self.client.like(media_id)

    def get_user_feed(self, user_id):
        """Получить последние записи пользователя"""
        self.client.getUserFeed(user_id)

    def get_media_comments(self, media_id):
        """Получить комментарии записи"""
        self.client.getMediaComments(media_id)

    def comment(self, media_id, comment_text):
        """Комментировать запись"""
        self.client.comment(media_id, comment_text)

    def last_json(self):
        return self.client.LastJson


#
# #----------получение id пользователей
# #api.searchUsername('robotixcorporation') #
# idFollowings = []
# idFollowers = []
#
#
# api.searchUsername('gruzzexpert')
# Id = api.LastJson['user']['pk']
# api.getUserFollowers(Id)
# nexter = True
# while nexter:
#         for a in api.LastJson['users']:
#             idFollowers.append(a['pk'])
#
#
#             nextid = api.LastJson.get('next_max_id')
#
#         if nextid:
#             api.getUserFollowers(Id, maxid = nextid)
#             time.sleep(random.uniform(1, 2))
#
#         else:
#             nexter = False
#
#
# print ('подписчиков ' + str(len(idFollowers)))
#
# unfoll = []
# unfoll = list(set(idFollowings) - set(idFollowers))
# ch = 0
# for un in unfoll:
#     api.unfollow(un)
#     ch = ch + 1
#     print ('отписок ' + str(ch))
#     time.sleep(random.uniform(35, 50))
#     if ch == 1000:
#         break
