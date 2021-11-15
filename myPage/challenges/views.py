from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
challenges = {
    "january": "This is January page",
    "february": "This is February page",
    "march": "This is March page",
    "april": "This is April page",
    "may": "This is May page",
    "june": "This is June page",
    "july": "This is July page",
    "august": "This is August page",
    "september": "This is September page",
    "october": "This is October page",
    "november": "This is November page",
    "december": "This is December page"
}


def index(request):
    return HttpResponse("This is Index page")


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month < 1 or month > len(months):
        return HttpResponseNotFound("<h1>" + "Out of value range!" + "</h1>")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenges_text = challenges[month]
        return HttpResponse("<h1>" + challenges_text + "<h1>")
    except:
        HttpResponseNotFound("This month is not suppurted!")

    # try:
    #     if month.isdigit() and (0 < int(month) < 13):
    #         challeng_text = list(challenges.values())
    #         return HttpResponse("<h1>" + challeng_text[(int(month)-1)] + "</h1>")
    #         # monthly_challenge(None, str(list(challenges)[month]))
    #     elif month.isdigit() and (12 < int(month) < 1):
    #         return HttpResponseNotFound("<h1>" + "This number is not supported!" + "</h1>")
    #     else:
    #         challeng_text = challenges[month]
    #         return HttpResponse("<h1>" + challeng_text + "</h1>")
    # except:
    #     return HttpResponseNotFound("<h1>" + "This value is not supported!" + "</h1>")
