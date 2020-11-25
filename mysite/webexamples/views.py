from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return HttResponse("<h3> Привет мир!</h3>")
# Create your views here.
