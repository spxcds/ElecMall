from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def index(request):
    return HttpResponse("I'm in customer");

def register(request):
    context = {}
    return render(request, "customer/register.html", context)

def login(request):
    context = {}
    return render(request, "customer/login.html", context)
