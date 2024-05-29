from django.db import models
import uuid
import datetime
from django.contrib.auth.models import User
# Create your models here.
class TourAgency(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    rating = models.IntegerField(default=5)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name

class Tour(models.Model):
    agency = models.ForeignKey(TourAgency, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    duration = models.PositiveIntegerField( null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    locations = models.TextField( null=True, blank=True)
    image_url = models.URLField( null=True, blank=True)

class TourBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class TourReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image_url = models.URLField()
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name