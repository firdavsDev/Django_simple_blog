from django.urls import path

from .views import *

urlpatterns = [
    path('create/', product_create_view),
    path('<int:id>/', dynamic_lookup_view,name="Product_list"),
    path('', product_view),
]