from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^account/$', include('accounts.urls')),
   # url(r'^login/$', login, {'template_name': 'accounts/login.html'})
]
