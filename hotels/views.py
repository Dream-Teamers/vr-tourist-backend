from django.shortcuts import render
from apis.serializers import HotelSerializer, RoomSerializer, RoomBookingSerializer
from rest_framework import generics
from .models import Hotel, Room, RoomBooking, HotelRating
# Create your views here.
class HotelListCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    
class HotelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'pk'


class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    
class RoomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'pk'
    
    
## Room Booking Views
class RoomBookingListCreate(generics.ListCreateAPIView):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    

class RoomBookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    lookup_field = 'pk'
    
    
## My Hotels View
class MyHotels(generics.ListAPIView):
    serializer_class = HotelSerializer
    
    def get_queryset(self):
        return Hotel.objects.filter(admin=self.request.user)
    
    
## view for my bookings
class MyBookings(generics.ListAPIView):
    serializer_class = RoomBookingSerializer
    
    def get_queryset(self):
        return RoomBooking.objects.filter(user=self.request.user)