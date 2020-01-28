from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("", include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
   # url(r'^account/', include('accounts.urls')),
   # url(r'^login/$', login, {'template_name': 'accounts/login.html'})
   # url('',include('accounts.urls')),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]