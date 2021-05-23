pip install git+git@github.com/RXcor/Instagram-API-python.git#egg=Instagram-API-python


Сервис автоматизации и сбора статитстики инстаграм

Deployment
Запуск flower
celery -A i_service flower --port=5555 --broker=redis://127.0.0.1:6379/0


Установка для разработки
- Установить Redis, PostgresQL

- Создать БД и пользователя с доступом в PostgreSQL.
- Создать файл .env, добавить туда переменные из env.example, прописать там логин-пароль до
PostgreSQL базы-данных.
- Создать и активировать виртуальное окружение c python 3.9.1 (если он не установлен, то так же нужно его установить)

$ virtualenv -p /usr/bin/python3.9.1 venv
или
$ python -m venv venv (если текущая версия pyton в системе 3.9.1 проверка $ python -V)

- Установить зависимости

$ pip instll -r requirements.txt

- Перейти в папку i_service и запустить миграции

cd i_service
./manage.py migrate

- Создать суперпользователя и попробовать запустить сервер

./manage.py createsuperuser

./manage.py runserver
