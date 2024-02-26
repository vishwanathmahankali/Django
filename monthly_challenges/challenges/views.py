from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")


# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes every day!")


# def march(request):
#     return HttpResponse("Learn Django for atleast 20 minutes every day!")


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn Django for atleast 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for atleast 20 minutes every day!",
    "june": "Learn Django for atleast 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for atleast 20 minutes every day!",
    "september": "Learn Django for atleast 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for atleast 20 minutes every day!",
    "december": "Learn Django for atleast 20 minutes every day!",
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    # if month == "january":
    #     challenge_text = "Eat no meat for the entire month!"
    # elif month == "february":
    #     challenge_text = "Walk for atleast 20 minutes every day!"
    # elif month == "march":
    #     challenge_text = "Learn Django for atleast 20 minutes every day!"
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not a valid!")
    