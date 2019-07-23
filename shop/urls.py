from django.urls import path
from .views import test, index, register, product, check_uniqueness, category, search

urlpatterns = [
    path('', index),
    path('test', test),
    path('register', register, name='register'),
    path('products/<product_slug>', product, name='product_page'),
    path('search', search, name='search'),
    path('categories/<category_slug>', category, name='category_page'),
    path('check-username/<username>', check_uniqueness, name='check_uniqueness')
]
