from django.shortcuts import render
from rest_framework import generics
from .models import AgencyRating, Tour, TourAgency, TourBooking
from apis.serializers import TourAgencySerializer, TourSerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apis.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class TourAgencyListCreate(generics.ListCreateAPIView):
    queryset = TourAgency.objects.all()
    serializer_class = TourAgencySerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    
    
class TourAgencyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourAgency.objects.all()
    serializer_class = TourAgencySerializer
    lookup_field = 'pk'
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    
class TourListCreate(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    
class TourRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'pk'
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    
class TourBookingListCreate(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
    
class TourBookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    lookup_field = 'pk'
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

