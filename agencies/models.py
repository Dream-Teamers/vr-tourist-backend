from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class TourAgency(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    description = models.TextField()

class Tour(models.Model):
    agency = models.ForeignKey(TourAgency, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    locations = models.TextField()
    image_url = models.URLField()

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