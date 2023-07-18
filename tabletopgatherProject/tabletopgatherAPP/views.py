from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from tabletopgatherAPP import views

# Create your views here.


def index(request):
    template = loader.get_template("home.html")

    return HttpResponse(template.render())