from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')