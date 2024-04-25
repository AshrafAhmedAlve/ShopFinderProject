from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True)


# models.py

from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    category=models.CharField(max_length=100, blank =True, null =True)
    address = models.CharField(max_length=200)
    phone_number=models.IntegerField(blank=True, null =True)
    description = models.TextField()
    image = models.ImageField(upload_to='shop_images/',blank=True, null=True, default='shop_images/default.jpg')
    shopping_complex = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=100)


    def __str__(self) :
        return self.name








