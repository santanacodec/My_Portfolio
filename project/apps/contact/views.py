#from django.http import HttpResponse
#from django.template import loader
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')

