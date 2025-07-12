from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to ReWear! This is the home page.")  
    return render(request, 'website/index.html')

def login(request):
    return render (request, 'website/login.html')
    

def signup(request):
    return render (request, 'website/signup.html')