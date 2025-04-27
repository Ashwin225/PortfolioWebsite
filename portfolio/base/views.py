from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . models import ContactMe
# Create your views here.

def home(request):
    if request.method=="POST":
        contact= ContactMe()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        content=request.POST.get('content')
        contact.name=name      #contact.model-name = name
        contact.email=email
        contact.phone=phone
        contact.content=content
        contact.save()
        return redirect('thankyou')


   
    return render(request,'home.html') #nammal inni oru create cheyanam eey request and response kanikan

def thankyou(request):
    return render(request,'thankyou.html')