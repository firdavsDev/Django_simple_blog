"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include


#saytga kirganda uzatiladigan yul

#ilovamizdan views impoert qilamiz
from pages import views

#Agar kup funksiyalar requestlar bulsa
from pages.views import home_view, contact

from products.views import product_view,product_create_view,render_initial_data,dynamic_lookup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # '' ichiga yul beramiz home/
    #view ichidagi  funksiya nomi
    # name='Bunga nom'

    path('blog/', include('blog.urls')),

    path('', views.home_view, name='home'),
    path('contact/', views.contact),
    path('create/', product_create_view),
    path('product/<int:id>/', dynamic_lookup_view,name="Product_list"),
    path('product/', product_view),
]
