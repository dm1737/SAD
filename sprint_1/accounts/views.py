from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .models import User
from django.contrib import messages
from django.core.mail import send_mail



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
        else:
            messages.error(request,'username or password not correct')
            return render(request = request,
                        template_name = "accounts/login.html",
                        context={"form":form})
    form = UserCreationForm
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@examplesever.com',
    ['dewonglucasjr@gmail.com'],
    fail_silently=False,
)
    return render(request = request,
                  template_name = "accounts/login.html",
                  context={"form":form})
    