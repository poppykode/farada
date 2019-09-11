from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class ParticipantSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","first_name","last_name","email","dob","phone_number","address","password1", "password2")
        widgets ={

        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_participant = True
        if commit:
            user.save()
        return user


class ProviderSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","first_name","last_name","ndis_number","services","city","phone_number","email" ,"password1", "password2")
        help_texts = {
            'username': None,
            'password': None,
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_provider = True
        if commit:
            user.save()
        return user