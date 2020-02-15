from django.contrib import admin
from .models import Tutorial, Post
from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class TutorialAdmin (admin.ModelAdmin):
    
    fields = ["title",
            "published",
            "content"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
# Register your models here.
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Post)



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)