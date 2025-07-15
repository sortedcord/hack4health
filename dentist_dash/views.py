from accounts.decorators import role_required
from django.shortcuts import render

@role_required(['dentist'])  # Assuming 'admin' is another role you want to allow
def dashboard_view(request):
    # Use template dentist_dash/index.html for the dentist dashboard
    return render(request, 'dentist_dash/index.html', {'user': request.user})    


@role_required(['dentist'])  # Assuming 'admin' is another role you want to allow
def manage_patients_view(request):
    # Use template dentist_dash/manage_patients.html for managing patients
    return render(request, 'dentist_dash/manage_patients.html', {'user': request.user})