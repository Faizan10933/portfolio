from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"index.html")

def index(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      message = request.POST.get('message')
      contact =  Contact(name=name, email=email, phone=phone, message=message, date= datetime.today())
      contact.save()
      # messages.success(request, 'Your message has been sent.')
    
    return render(request,'')