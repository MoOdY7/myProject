# Create your views here.
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from .models import *
from .forms import ContactForm 
from myApp.forms import LoginForm , CustomerRegistrationForm

class CustomerRegistratioinView(View):
   def get(self, request):
      form = CustomerRegistrationForm()
      return render(request, 'signup.html', {'form':form})
   def post(self, request):
      form = CustomerRegistrationForm(request.POST)
      if form.is_valid():
         messages.success(request, 'Congratulations!! Registration Sucsessfully')
         form.save()
      return render(request, 'signup.html', {'form':form})

def HandleIndex(request):
    return render(request, 'index.html')

class ProductView(View):
    def get(self, request):
        home_appliances = Product.objects.filter(category = 'HA')
        cosmetics_gadgets = Product.objects.filter(category = 'G')
        return render(request, 'service.html', {"home_appliances":home_appliances, "cosmetics_gadgets": cosmetics_gadgets})
  
class ProductDetailView(View):
  def get(self, request, pk):
    product = Product.objects.get(pk =pk)
    return render(request, 'productdetail.html',{'product':product})
  
def homeappliances(request, data=None):
    if data is None:
        homeappliances = Product.objects.filter(category='HA')
    elif data == 'Samsung' or data == 'LG' or data == 'Sony' or data == 'Whirlpool' or data == 'Philips': 
        homeappliances = Product.objects.filter(category='H', brand=data)
    return render(request, 'homeappliances.html', {'homeappliances': homeappliances})

def feature(request):
    feature = Product.objects.filter(category='W')
    return render(request, 'feature.html', {'feature': feature})

def about(request):
    return render(request, 'aboutus.html', {'about': about})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False) 
            contact.save()
            messages.success(request, "Message sent successfully")
            return redirect('contact')  
    else:
        form = ContactForm()  

    return render(request, 'contact.html', {'form': form})


def cosmetics(request):
    cosmetics = Product.objects.filter(category='G')
    return render(request, 'cosmetics.html', {'cosmetics': cosmetics})