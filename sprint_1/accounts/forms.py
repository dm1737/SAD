from django import forms
from django.forms import BaseFormSet, formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Journal
from decimal import *
from .models import Journal, Account, Journal, Statement
from django.utils.translation import gettext_lazy as _

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
            'Type',
            #'journal_balance',
            #'source_document'
        ]
        labels = {
            'text': _('Writer'),
        }
        widgets = {
            
            'account': forms.Select(
                attrs={
                    'class': 'form-control'
                    }                
                ),
            'Journal_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            
            'Journal_number': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'Journal_description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'initial_journal_balance': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'journal_debit': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'journal_credit': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'journal_balance': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'source_document': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
                'Type': forms.Select(
                attrs={
                    'class': 'form-control'
                    }                
                ),
             
            }

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

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'account_name',
            'debit',
            'credit',
        ]
class StatementsForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = [
            'Total_debit',
            'Total_Credit',
        ]
