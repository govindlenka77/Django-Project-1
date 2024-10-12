from django.urls import path
from .views import *
urlpatterns = [
    path('hello/',say_hello,name='say_hello'),
    path('say_bye/',say_bye, name='say_bye'),
]
