from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dentist_dash.models import DentistProfile
from .forms import DentistSignUpForm

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
            user = form.save(commit=False)
            user.role = 'dentist'
            user.save()
            # Also create the DentistProfile instance
            DentistProfile.objects.create(user=user)
            messages.success(request, 'Dentist account created. You can now log in.')
            return redirect('login')
    else:
        form = DentistSignUpForm()
    return render(request, 'accounts/register_dentist.html', {'form': form})


@login_required
def role_dashboard_redirect(request):
    if hasattr(request.user, 'role') and request.user.role == 'dentist':
        return redirect('/dash/dentist')
    else:
        return redirect('/dash/user')
