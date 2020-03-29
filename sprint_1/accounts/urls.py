from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf.urls import url
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
    path("adjusting_journals/", views.adjusting_journals, name="adjusting_journals"),
	path("forgot_password/", views.fgtpassword, name="fgtpassword"),
    path("journal_view/", views.journal_view, name="journal_view"),
    path("journal_view/<int:id>",views.journal_view, name="journal_view"),
    path("manage_journals/", views.manageJournals, name="managejournals"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)