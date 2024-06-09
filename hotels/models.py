from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Hotel(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    amenities = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    rooms = models.ManyToManyField('Room', related_name='rooms', blank=True)
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
    room_type = models.CharField(max_length=200, default = 'Single Room')
    occupancy = models.IntegerField(default=1)  # Set a default value for occupancy
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)    
    availability = models.BooleanField(default=True)
    images = models.ForeignKey('RoomImage', on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.room_type


class RoomImage(models.Model):
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    

class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)