from django.shortcuts import render
from django.http import response

# Create your views here.


def index(request):
    return response.HttpResponse("This is Index page")


def january(request):
    return response.HttpResponse("This is January page")


def february(request):
    return response.HttpResponse("February works good!")
