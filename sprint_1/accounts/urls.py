from django.contrib.auth.views import LoginView
from django.conf.urls import url
from django.urls import path
from . import views

#app_name = "users"

urlpatterns = [
    url(r'^$', LoginView.as_view(template_name='accounts/login.html'), name="login"),
]