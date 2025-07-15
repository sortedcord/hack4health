from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

User = get_user_model()

class DentistSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')  # Add more as needed

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'dentist'
        if commit:
            user.save()
        return user

def register_dentist(request):
    if request.method == 'POST':
        form = DentistSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dentist account created successfully. You can now log in.')
            return redirect('login')  # Change to your login route
    else:
        form = DentistSignUpForm()
    return render(request, 'accounts/register_dentist.html', {'form': form})
