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

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShopForm
from .models import Shop

def update_shop(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_listing')  # Redirect to shop listing page
    else:
        form = ShopForm(instance=shop)
    return render(request, 'create_shop.html', {'form': form})


def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    return render(request, 'shop_detail.html', {'shop': shop})






