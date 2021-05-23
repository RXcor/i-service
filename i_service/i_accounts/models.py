from django.db import models
from i_auth.models import User

# Create your models here.
class Account(models.Model):

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True, )
    ip_address = models.CharField(max_length=30, null=True, blank=True)
    like_limit_for_job = models.IntegerField(blank=True, null=True)
    follow_limit_for_job = models.IntegerField(blank=True, null=True)
    unfollow_limit_for_job = models.IntegerField(blank=True, null=True)
    comment_limit_for_job = models.IntegerField(blank=True, null=True)
    is_busines = models.BooleanField(default=False)
    instagram_id = models.CharField(max_length=20, blank=True, null=True)
    device_id = models.CharField(max_length=30, null=True, blank=True)
    username_id = models.BigIntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=40, null=True, blank=True)
    isLoggedIn = models.BooleanField(default=False, null=True, blank=True)
    token = models.CharField(max_length=40, null=True, blank=True)
    sessionid = models.CharField(max_length=40, null=True, blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def dict_for_ws(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'current_state': self.current_state,
        }

    def last_session_data(self):
        return {
            'username': self.username,
            'password': self.password,
            'device_id': self.device_id,
            'username_id': self.username_id,
            'uuid': self.uuid,
            'token': self.token,
            'sessionid': self.sessionid,
            'isLoggedIn': self.isLoggedIn
        }
