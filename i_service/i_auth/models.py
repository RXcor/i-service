from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import PermissionsMixin, AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from django_paranoid.models import ParanoidModel



class CustomUserManager(UserManager):

    def get_by_natural_key(self, username):
        return self.get(
            models.Q(**{self.model.USERNAME_FIELD: username}) |
            models.Q(**{self.model.EMAIL_FIELD: username})
        )

class User(AbstractUser, ParanoidModel):
    balance = models.IntegerField(default=1000)

    objects = CustomUserManager()
    
