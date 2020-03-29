from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
from simple_history.admin import SimpleHistoryAdmin
from .models import UserAccount
from .models import Journal, AdjustingJournalEntry


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


class JournalAdmin(SimpleHistoryAdmin):
    
    list_display = (
                    "account",
                    "Journal_name",
    				"Journal_number",
    				"Journal_description",
    				"initial_journal_balance",
    				"journal_debit",
                    "journal_credit",
    				"journal_balance",
                    "status")
    search_fields = ['Journal_name','Journal_number', 'Journal_description']


class AdjustingJournalAdmin(SimpleHistoryAdmin):
    
    list_display = (
                    "account",
                    "Adjusted_journal_name",
    				"Adjusted_journal_number",
    				"Adjusted_journal_description",
    				"Adjusted_journal_debit",
                    "Adjusted_journal_credit",
                    "Adjusted_status")
    search_fields = ['Adjusted_journal_name','Adjusted_journal_number', 'Adjusted_journal_description']


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserAccount, AccountAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(AdjustingJournalEntry, AdjustingJournalAdmin)