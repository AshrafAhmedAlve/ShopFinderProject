"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ShopFinder.views import *

urlpatterns = [

    path('', ShopFinder, name="ShopFinder"),
    path('signinoptions/', signinOptions, name="SignIn Options"),
    path('signin/', SignIn, name="SignIn"),
    path('signup/', SignUp, name="SignUp"),
    path('aboutus/', AboutUs, name="AboutUs"),
    path('userdashboard/', UserDashboard, name="User Dashboard"),
    path('shopownerdash/', ShopOwnerDashboard, name='Shop Owner Dashboard'),
    path('shoplisting/', shop_listing, name='shop_listing'),
    path('addshopform/', create_shop, name='create_shop'),
    path('admin/', admin.site.urls),
]
