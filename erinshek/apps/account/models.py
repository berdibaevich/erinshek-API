from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    REQUIRED_FIELDS = [] # Removed email field..

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
