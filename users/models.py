from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    contact_info = models.CharField(max_length=100, null=True, blank=True)

    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    card_holder_name = models.CharField(max_length=255)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    billing_address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.PositiveIntegerField()
    type = models.CharField(max_length=20)  # Choices: hotel, tour, vr_experience

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20)  # e.g., login, logout, booking, review
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    username = models.CharField(max_length=50,null=True, blank=False)
    email = models.EmailField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    contact_info = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/user.png', null=True, blank=True)
    password = models.CharField(max_length=200,null=True)
    password_confirmation = models.CharField(max_length=100,null=True)


class HelpSupport(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    
