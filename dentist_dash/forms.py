from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class PatientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded'}),
            # Add similar widgets for other fields if desired
        }

    # If you want to customize email field widget
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     'class': 'w-full px-4 py-2 border border-gray-300 rounded'
    # }))
