from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse("This is Index page")


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challeng_text = None

    if month == "january":
        challeng_text = "This is January page"
    elif month == "february":
        challeng_text = "This is February page"
    elif month == "march":
        challeng_text = "This is March page"
    else:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    return HttpResponse(challeng_text)
