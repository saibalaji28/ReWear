from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to ReWear! This is the home page.")  
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("About ReWear: We are committed to sustainable fashion and reducing textile waste. Join us in our mission!")

def contact(request):
    return HttpResponse("Contact ReWear: info@rewear.com")  