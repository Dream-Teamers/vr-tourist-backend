from django.shortcuts import render
from .models import VR, VRBooking, VRRating
from apis.serializers import VRSerializer, VRBookingSerializer, VRRatingSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from apis.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class VRListCreate(generics.ListCreateAPIView):
    queryset = VR.objects.all()
    serializer_class = VRSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
class VRRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VR.objects.all()
    serializer_class = VRSerializer
    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    


class VRList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request, format=None):
        # Get the title form the query
        title = request.query_params.get('title', '')
        
        if title:
            vr = VR.objects.filter(title__icontains = title)
            
        else:
            vr = VR.objects.all()
            

        serializer = VRSerializer(vr, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class VRBookingListCreate(generics.ListCreateAPIView):
    queryset = VRBooking.objects.all()
    serializer_class = VRBookingSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
class VRBookingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VRBooking.objects.all()
    serializer_class = VRBookingSerializer
    lookup_field = 'pk'
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    
class VRRatingListCreate(generics.ListCreateAPIView):
    queryset = VRRating.objects.all()
    serializer_class = VRRatingSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
class VRRatingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VRRating.objects.all()
    serializer_class = VRRatingSerializer
    lookup_field = 'pk'
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]