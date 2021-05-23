from django.db import models
from i_accounts.models import Account

from django.dispatch import Signal

from django.db.models.signals import post_save
from django.dispatch import receiver


job_create_signal = Signal(providing_args=['id'])

job_update_signal = Signal(providing_args=['id'])

# Create your models here.
class Job(models.Model):

    TYPES = (
        (0, 'Лайки по лайктайму'),
        (1, 'Лайки по хэштегам'),
        (2, 'Подписки по хэштегам'),
        (3, 'Отписка от неподписаных'),
        (4, 'Отписка от всех'),
        (5, 'Игра'),
        (6, 'Розыгрыш')
    )

    TYPES_PSEUDO = {
        3: 'unfollow_from_not_followers'
    }

    type_of = models.IntegerField(choices=TYPES, blank=False)
    data = models.CharField(max_length=255, null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL)
    progress = models.IntegerField(blank=True, null=True)
    vinner = models.CharField(max_length=255, null=True, blank=True)
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}-{self.type_of}'

    def dict_for_ws(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'current_state': self.current_state,
        }

@receiver(post_save, sender=Job)
def signal_send(sender, instance, created, **kwargs):
    if created:
        job_create_signal.send(sender=sender, id=instance.id)
    else:
        job_update_signal.send(sender=sender, id=instance.id)
