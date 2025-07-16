from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('high', 'High'),
        ('emergency', 'Emergency'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    # Add more patient-specific fields as needed

    def __str__(self):
        return f'UserProfile: {self.user.username}'


class TestReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test_id = models.CharField(max_length=100, unique=True)
    test_date = models.DateTimeField(auto_now_add=True)
    final_score = models.FloatField(blank=True, null=True)
    test_data = models.JSONField(blank=True, null=True)  # Store test data as JSON
    highlights = models.TextField(blank=True, null=True)  # Store highlights or important notes
    approved = models.BooleanField(default=False)
    status = models.TextField(max_length=255, default="in_progress")
    image = models.ImageField(upload_to='test_reports/', blank=True, null=True)
    

    def __str__(self):
        return f'TestReport: {self.test_id} for {self.user.username} on {self.test_date}'
    
    def generate_id(self):
        import uuid
        self.test_id = str(uuid.uuid4())
        self.save()
