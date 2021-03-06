from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from django_paranoid.models import ParanoidModel


class User(AbstractUser, ParanoidModel):
    balance = models.IntegerField(default=1000)
    
