from django.shortcuts import render
from rest_framework import generics
from .models import AgencyRating, Tour, TourAgency, TourBooking
from apis.serializers import TourAgencySerializer, TourSerializer, TourBookingSerializer

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
    queryset = TourBooking.objects.all()
    serializer_class = TourBookingSerializer
    
class TourBookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourBooking.objects.all()
    serializer_class = TourBookingSerializer
    lookup_field = 'pk'
    

#view for my tours
class MyTours(generics.ListAPIView):
    serializer_class = TourBookingSerializer
    
    def get_queryset(self):
        print(self.request.user)
        return TourBooking.objects.filter(user=self.request.user)
    
# view for my agencies
class MyAgencies(generics.ListAPIView):
    serializer_class = TourAgencySerializer
    
    def get_queryset(self):
        return TourAgency.objects.filter(admin=self.request.user)
    