from accounts.decorators import role_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import PatientCreationForm
from user_dash.models import UserProfile
from .models import DentistProfile

User = get_user_model()

@role_required(['dentist'])  # Assuming 'admin' is another role you want to allow
def dashboard_view(request):
    # Use template dentist_dash/index.html for the dentist dashboard
    return render(request, 'dentist_dash/index.html', {'user': request.user})    


@role_required(['dentist'])
def manage_patients_view(request):
    # Get the DentistProfile for this logged-in user
    dentist_profile = DentistProfile.objects.get(user=request.user)

    # Fetch patients associated with this dentist
    patients = dentist_profile.patients.all()  # Assuming a M2M to CustomUser

    return render(request, 'dentist_dash/manage_patients.html', {
        'patients': patients,
    })

@role_required(['dentist'])
def create_patient(request):
    if request.method == 'POST':
        form = PatientCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'
            user.save()
            # Create a UserProfile for this user
            UserProfile.objects.create(user=user)
            # Optionally associate with dentistprofile
            request.user.dentistprofile.patients.add(user)
            return redirect('manage_patients')
    else:
        form = PatientCreationForm()
    return render(request, 'dentist_dash/create_patient.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, "Patient deleted successfully.")
        return redirect('manage_patients')  # Change to your patient list view name

    # Optional: Render a confirmation page/template
    return render(request, 'dentist_dash/delete_user_confirm.html', {'user': user})

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = PatientCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient updated successfully.")
            return redirect('manage_patients')  # Change to your patient list view name
    else:
        form = PatientCreationForm(instance=user)

    return render(request, 'dentist_dash/edit_user.html', {'form': form, 'user': user})