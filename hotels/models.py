from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    amenities = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    rooms = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class HotelRating(models.Model):
    VOTE_TYPE = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, choices=VOTE_TYPE, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.value}"
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    locations = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    

class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)