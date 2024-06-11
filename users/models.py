from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserAccount(models.Model):
    ROLE_CHOICES = (
        ('tourist', 'Tourist'),
        ('tour_agency', 'Tour Agent'),
        ('hotel', 'Hotel Manager'),
        ('admin', 'System Administrator'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default='tourist')
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

