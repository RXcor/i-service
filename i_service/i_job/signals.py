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
        raffle_task.delay(job_instance.data, 2)

@receiver(job_update_signal)
def send_status(sender, **kwargs):
    job_instance = Job.objects.get(id=kwargs['id'])
    print(job_instance.progress)
