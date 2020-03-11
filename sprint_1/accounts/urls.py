from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import ManageJournals

app_name = 'accounts'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("profile/", views.profile, name="profile"),
    path("help/", views.help, name="help"),
    path("ledger/", views.ledger, name="ledger"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("accounts/", views.view_account, name="account"),
    path("journals/", views.journals, name="journals"),
	path("forgot_password/", views.fgtpassword, name="fgtpassword"),
    #path("manage_journals/", ManageJournals.as_view(), name="journal-create"),
    path("manage_journals/", views.manageJournals, name="managejournals"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)