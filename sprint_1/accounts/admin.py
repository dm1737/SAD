from django.contrib import admin
from .models import Tutorial, Post
from tinymce.widgets import TinyMCE
from django.db import models

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


