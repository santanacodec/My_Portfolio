#from django.http import HttpResponse
#from django.template import loader
import bleach
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from project import settings

from.forms import ContactForm

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET": 
        form = ContactForm()        
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            email = bleach.clean(form.cleaned_data["email"])
            message = bleach.clean(form.cleaned_data["message"])
            send_mail(f"{name} sent an email", message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, 'contact.html', {"form": form, "success": True})
    else:
        raise NotImplementedError
    return render(request, 'contact.html', {"form": form})


