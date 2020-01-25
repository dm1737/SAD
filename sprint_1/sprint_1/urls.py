#from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('accounts.urls')),
    #url(r'^account/', include('accounts.urls')),
   # url(r'^login/$', login, {'template_name': 'accounts/login.html'})
]
