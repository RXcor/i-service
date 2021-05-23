pip install git+git@github.com/RXcor/Instagram-API-python.git#egg=Instagram-API-python


Сервис автоматизации и сбора статитстики инстаграм
Запуск flower
celery -A i_service flower --port=5555 --broker=redis://127.0.0.1:6379/0

Не запускаются фоновые задачи после попытки исправить циклический импорт
