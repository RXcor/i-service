from django.db import models
from i_auth.models import User

# Create your models here.
class Account(models.Model):

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=512, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True, )
    ip_address = models.CharField(max_length=30, null=True, blank=True)
    like_limit_for_job = models.IntegerField(blank=True, null=True)
    follow_limit_for_job = models.IntegerField(blank=True, null=True)
    unfollow_limit_for_job = models.IntegerField(blank=True, null=True)
    comment_limit_for_job = models.IntegerField(blank=True, null=True)
    is_busines = models.BooleanField(default=False)

    def __str__(self):
        return self.login

    def dict_for_ws(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'current_state': self.current_state,
        }
