from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home page")


def say_hello(request):
    return HttpResponse("Hello world")

def say_bye(request):
    return HttpResponse("Bye!!!!!")

