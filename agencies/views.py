from django.shortcuts import render
from rest_framework import generics
from .models import AgencyRating, Tour, TourAgency, TourBooking
from apis.serializers import TourAgencySerializer, TourSerializer

# Create your views here.
class TourAgencyListCreate(generics.ListCreateAPIView):
    queryset = TourAgency.objects.all()
    serializer_class = TourAgencySerializer
    
    
class TourAgencyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourAgency.objects.all()
    serializer_class = TourAgencySerializer
    lookup_field = 'pk'
    
class TourListCreate(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    
class TourRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'pk'
    
class TourBookingListCreate(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    
class TourBookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'pk'
    

