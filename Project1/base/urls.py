from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('say_hello/',say_hello,name='say_hello'),
    path('say_bye/',say_bye, name='say_bye'),
]
