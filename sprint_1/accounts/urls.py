from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    #url(r'^$', LoginView.as_view(template_name='accounts/login.html'), name="home"),
    #url('/home/', LoginView.as_view(template_name='accounts/home.html'), name="home"),
]