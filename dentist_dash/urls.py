from django.urls import path
from .views import dashboard_view, manage_patients_view, create_patient


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('/patients', manage_patients_view, name='manage_patients'),
    path('/patients/add', create_patient, name='create_patient'),
]