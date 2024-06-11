from django.contrib import admin
from .models import Hotel, HotelRating, Room, RoomImage, Tag

# Register your models here.
admin.site.register(Hotel)
admin.site.register(HotelRating)
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(Tag)

