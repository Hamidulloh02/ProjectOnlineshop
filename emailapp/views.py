from django.shortcuts import render
from .models import SendEmail
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def SendEmail1(request):
    if request.method == "POST":
        name = request.POST["title"]
        poster = request.POST["poster"]
        text = request.POST["text"]
        url = request.POST["url"]
        send_mail(name,text,url,['hamidullonematullayev22@gmail.com'],fail_silently=False)
    return render(request,'SendEmail')
