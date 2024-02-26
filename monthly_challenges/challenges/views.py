from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"""
        <ul>
            {list_items}
        </ul>
    """
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    # if month == "january":
    #     challenge_text = "Eat no meat for the entire month!"
    # elif month == "february":
    #     challenge_text = "Walk for atleast 20 minutes every day!"
    # elif month == "march":
    #     challenge_text = "Learn Django for atleast 20 minutes every day!"

        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not a valid!</h1>")
