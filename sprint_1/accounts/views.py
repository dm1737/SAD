from django.shortcuts import render, HttpResponse

def landingPage(request):
    return render(request, 'accounts/login.html')
def home(request):
    return render(request, 'accounts/home.html')
