from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class DentistSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # List all required fields; add more as needed
        fields = ('username', 'email', 'first_name', 'last_name')
