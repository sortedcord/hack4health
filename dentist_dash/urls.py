from django.urls import path
from .views import dashboard_view, manage_patients_view


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('patients', manage_patients_view, name='manage_patients'),
]