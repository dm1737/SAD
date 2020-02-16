from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("forgot_password/", views.fgtpassword, name="fgtpassword"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
