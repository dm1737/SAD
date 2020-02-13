from django.contrib import admin
from .models import Post, UserAccount
from tinymce.widgets import TinyMCE
from django.db import models
from simple_history.admin import SimpleHistoryAdmin


class TutorialAdmin (admin.ModelAdmin):
    
    fields = ["title",
            "published",
            "content"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
# Register your models here.
admin.site.register(UserAccount, SimpleHistoryAdmin)


