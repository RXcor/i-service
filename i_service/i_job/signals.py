from .models import Job, job_create_signal, job_update_signal

from django.dispatch import receiver
from i_job.tasks import raffle_task

print('signals is imported')

@receiver(job_create_signal)
def run_task(sender, **kwargs):
    job_instance = Job.objects.get(id=kwargs['id'])
    print(job_instance)
    if job_instance.type_of == 6:
        #розыгрыш
        #Добавить в модель поле параметр и оттуда брать 2


        url = job_instance.data.get('url', None)
        winners_count = job_instance.data.get('winners_count', 1)
        exclude_masfollowers = job_instance.data.get('exclude_masfollowers', False)
        min_media_count = job_instance.data.get('min_media_count', True)
        winners_is_followers = job_instance.data.get('winners_is_followers', False)

        raffle_task.delay(url,
            winners_count=winners_count,
            exclude_masfollowers=exclude_masfollowers,
            min_media_count=min_media_count,
            winners_is_followers=winners_is_followers)



@receiver(job_update_signal)
def send_status(sender, **kwargs):
    job_instance = Job.objects.get(id=kwargs['id'])
    print(job_instance.progress)
