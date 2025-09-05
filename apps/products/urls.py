from django.urls import path

from apps.products.views import products_list_view

app_name = 'products'

urlpatterns = [
    path('', products_list_view, name='list'),
]
