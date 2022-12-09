from django.db import models

from account.models import User
# Create your models here.


class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

