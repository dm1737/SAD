#from django.contrib.auth.views import LoginView
#from django.conf.urls import url
#from django.urls import path
from django.urls import path, include
#from . import views
from accounts import views as user_views


urlpatterns = [
    path('', user_views.home, name="home"),
    #url('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('login/', user_views.login, name="login"),
    path('register/', user_views.register, name='register'),
]   
