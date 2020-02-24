from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
from simple_history.admin import SimpleHistoryAdmin
from .models import UserAccount


class AccountAdmin (SimpleHistoryAdmin):
    
    list_display = (
    	            "account_name",
    				"account_number",
    				"account_category",
    				"debit",
    				"credit",
    				"balance")
    search_fields = ['account_number','account_name']
    
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
admin.site.register(UserAccount, AccountAdmin)