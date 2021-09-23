from django.contrib import admin

# Register your models here.

#baza model.py yasab bulgach uni admin faylga ulaymiz
from .models import Product

admin.site.register(Product)