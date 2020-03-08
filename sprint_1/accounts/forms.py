from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Journal

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
            'initial_journal_balance',
            'journal_debit',
            'journal_credit',
            'journal_balance',
            'source_document'
        ]