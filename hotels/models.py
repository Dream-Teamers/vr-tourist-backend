from django.db import models
from django.contrib.auth.models import User


import uuid
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    # rating = models.IntegerField(default=5)
    locations = models.TextField(null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    # rooms = models.ManyToManyField('Room', blank=True)
    
    def __str__(self) -> str:
        return self.name
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    occupancy = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    total_rooms = models.IntegerField(default=0)  # Add this line
    available_rooms = models.IntegerField(default=0)  # Add this line

class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class RoomReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

# class RoomImage(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     image_url = models.URLField()
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class HotelRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user.username} - {self.rating}"
    
    