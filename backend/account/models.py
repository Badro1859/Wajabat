from django.db import models

from django.contrib.auth.models import AbstractUser


# AbastractUser class attributes :
# username, firstname, lastname, email, password
class User(AbstractUser):
    
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField(max_length=200, blank=True, null=True)
     
