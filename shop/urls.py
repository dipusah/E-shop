from django.urls import path
from .views import test, index, register

urlpatterns = [
    path('', index),
    path('test', test),
    path('register', register, name='register')
]
