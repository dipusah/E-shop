from django.urls import path
from .views import test, index, register, product

urlpatterns = [
    path('', index),
    path('test', test),
    path('register', register, name='register'),
    path('products/<product_slug>', product, name='product_page')
]
