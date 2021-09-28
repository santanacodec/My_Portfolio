#from django.http import HttpResponse
#from django.template import loader
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def portfolio(request: HttpRequest) -> HttpResponse:
    return render(request, 'portfolio.html')
