from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_CHOICES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
        ('billing', 'Billing Inquiry'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    attached_file = models.FileField(upload_to='requests/', null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} - {self.status}"
