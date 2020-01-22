from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .models import User

def home(request):
    return render(request, 'accounts/home.html')
def login_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("accounts:home")
    form = UserCreationForm
    return render(request = request,
                  template_name = "accounts/login.html",
                  context={"form":form})
    