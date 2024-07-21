from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    web_site = models.URLField(max_length=200, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']