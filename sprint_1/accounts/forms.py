from django import forms
from django.forms import BaseFormSet, formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Journal
from decimal import *

from .models import Journal, AdjustingJournalEntry, UserAccount, Journal, Statements
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class EmailForm(forms.Form):
    email = forms.EmailField(required=True)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        emailset = User.objects.filter(email=email)
        if emailset.exists():
            return email
        else:
            return None


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = [
            'account',
            'Journal_name',
            'Journal_number',
            'Journal_description',
            #'initial_journal_balance',
            'journal_debit',
            'journal_credit',
            #'journal_balance',
            'source_document'
        ]

class JournalFormset(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        balance = 0
        for form in self.forms:
            debit = form.cleaned_data.get('journal_debit')
            credit = form.cleaned_data.get('journal_credit')
            balance += debit
            balance -= credit
        if balance != 0:
            raise forms.ValidationError('Journal Entries must have a balance of 0')

class AdjustingJournalForm(forms.ModelForm):
    class Meta:
        model = AdjustingJournalEntry
        fields = [
            'account',
            'Adjusted_journal_name',
            'Adjusted_journal_number',
            'Adjusted_journal_description',
            'Adjusted_journal_debit',
            'Adjusted_journal_credit',
            'Adjusted_source_document'
        ]
class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'account_name',
            'debit',
            'credit',
        ]
class StatementsForm(forms.ModelForm):
    class Meta:
        model = Statements
        fields = [
            'Total_debit',
            'Total_Credit',
        ]

