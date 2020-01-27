from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request): 
    form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})