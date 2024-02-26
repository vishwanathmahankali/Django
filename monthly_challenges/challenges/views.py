from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")


# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes every day!")


# def march(request):
#     return HttpResponse("Learn Django for atleast 20 minutes every day!")

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for atleast 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for atleast 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not a valid!")
    return HttpResponse(challenge_text)