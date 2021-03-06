Сервис автоматизации и сбора статитстики инстаграм
Запуск flower
celery -A i_service flower --port=5555 --broker=redis://127.0.0.1:6379/0
