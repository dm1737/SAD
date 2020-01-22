from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.login_request, name="login_request"),
    path('login/', views.login_request, name="login_request"),
    path("home/", views.home, name="home")
]