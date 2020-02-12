from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Tutorial, Post, Profile
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Profile
class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'user'
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)
class TutorialAdmin (admin.ModelAdmin):
    
    fields = ["title",
            "published",
            "content"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Post)


