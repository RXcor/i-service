from django.db import models
from i_accounts.models import Account

# Create your models here.
class Job(models.Model):

    TYPES = (
        (0, 'Лайки по лайктайму'),
        (1, 'Лайки по хэштегам'),
        (2, 'Подписки по хэштегам'),
        (3, 'Отписка от неподписаных'),
        (4, 'Отписка от всех'),
        (5, 'Игра')
    )

    TYPES_PSEUDO = {
        3: 'unfollow_from_not_followers'
    }

    type_of = models.IntegerField(choices=TYPES, blank=False)
    data = models.CharField(max_length=255, null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True)
    is_complete = models.BooleanField(default=False)
    account = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.login

    def dict_for_ws(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'current_state': self.current_state,
        }
