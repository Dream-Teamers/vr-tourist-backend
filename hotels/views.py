from django.shortcuts import render
from apis.serializers import HotelSerializer
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