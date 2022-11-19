from django.db import models

from django.contrib.auth.models import AbstractUser


# AbastractUser class attributes :
# username, firstname, lastname, email, password
class User(AbstractUser):
    pass