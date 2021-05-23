from django.apps import AppConfig


class IJobConfig(AppConfig):
    name = 'i_job'

    def ready (self):
        import i_job.signals
