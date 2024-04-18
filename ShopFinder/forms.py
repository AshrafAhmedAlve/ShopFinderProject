from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'category', 'address', 'phone_number', 'description', 'image', 'shopping_complex', 'district']
