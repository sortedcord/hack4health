from django.db import models
from django.conf import settings


class DentistProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    clinic_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=100)
    patients = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='dentists',
        limit_choices_to={'role': 'patient'},  # Match your CustomUser role label!
        blank=True,
    )

    def __str__(self):
        return f'DentistProfile: {self.user.username}'

    
class Appointment(models.Model):
    dentist = models.ForeignKey(DentistProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Appointment: {self.dentist.user.username} with {self.patient.username} on {self.appointment_date}'
    
    
# Report
# 