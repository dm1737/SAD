from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("forgot_password/", views.fgtpassword, name="fgtpassword"),
    #url(r'^$', LoginView.as_view(template_name='accounts/login.html'), name="home"),
    #url('/home/', LoginView.as_view(template_name='accounts/home.html'), name="home"),
]
