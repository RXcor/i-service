import requests
import json
import uuid
import logging
from i_service.env import env
from i_job.models import Job

__all__ = ["Proxy"]

logger = logging.getLogger(__name__)

class Proxy:
    '''Проксирование ссылок с хранением данных на собственном сервере'''
    def __init__(self, job_id):
        self.job = Job.objects.get(id = job_id)

    def replace_urls(self):
        dict_data = json.loads(json.dumps(self.job.result))
        proxykeys = ['profile_pic_url']
        #Поиск адреса ссылок в полученных данных
        for proxykey in proxykeys:
            #Перебор проксируемых ключей
            paths_to_finded = self._find_key(proxykey, dict_data)
            print('len finded', len(paths_to_finded))
            if len(paths_to_finded) == 0:
                continue
            else:
                #Для каждого ключа проксировать и заменить ссылку
                #По полученному адресу получить исходный url и заменить на прокси
                for path_to_finded in paths_to_finded:
                    codestring = 'dict_data'
                    for key in path_to_finded:
                        if isinstance(key, int):
                            codestring += f"[{key}]"
                        else:
                            codestring += f"['{key}']"
                    new_file_name = f"{str(uuid.uuid4())}.jpg"
                    new_url = self._proxy_image(eval(codestring), new_file_name)
                    #Подмена
                    codestring += ' = new_url'
                    exec(codestring)
                self.job.result = dict_data
                self.job.save()

    @staticmethod
    def _find_key(key, dict_data):
        '''Поиск адреса ключа по словарю'''
        print(f"start find {key}")
        def getindexesfromlist(data, stack):
            for k, v in enumerate(data):
                k2 = [k] + stack
                yield k2
                if v and isinstance(v, dict):
                    for c in getkeysfromdict(v, k2):
                        yield c
        def getkeysfromdict(dict_data, stack):
            for k, v in dict_data.items():
                k2 = ([k] if k else []) + stack
                if v and isinstance(v, dict):
                    for c in getkeysfromdict(v, k2):
                        yield c
                elif v and isinstance(v, list):
                    for c in getindexesfromlist(v, k2):
                        yield c
                else:
                    yield k2
        findeds = []
        for keys_list in getkeysfromdict(dict_data, []):
            if key in keys_list:
                keys_list.reverse()
                findeds.append(keys_list)
        return findeds

    @staticmethod
    def _proxy_image(url, name):
        #сохранение картинки  и возврат нового url
        images_dir = env('PROXY_IMAGES_DIR')
        images_url = env('PROXY_IMAGES_URL')
        filepath = '/'.join([images_dir, name])
        r = requests.get(url)
        file = open(filepath, 'wb')
        file.write(r.content)
        file.close()
        fileurl = '/'.join([images_url, name])

        return fileurl
