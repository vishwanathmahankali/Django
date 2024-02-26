from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for the entire month!")


def february(request):
    return HttpResponse("Walk for atleast 20 minutes every day!")