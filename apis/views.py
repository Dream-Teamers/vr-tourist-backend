from rest_framework.decorators import api_view
from rest_framework.response import Response
from vr_experience.models import VRExperience, VRRating
from hotels.models import Hotel, Room
from agencies.models import TourAgency
from django.contrib.auth.models import User
from users.models import UserAccount
from .serializers import VRSerializer, HotelSerializer, TourAgencySerializer, UserAccountSerializer, UserSerializer, RoomSerializer
import json

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token






class HotelListCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def get(self, request, format=None):
        # Get the title form the query
        title = request.query_params.get('title', '')
        
        if title:
            hotel = Hotel.objects.filter(name__icontains = title)
            
        else:
            hotel = Hotel.objects.all()
            

        serializer = HotelSerializer(hotel, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class HotelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'pk'

class HotelList(APIView):
    def get(self, request, format=None):
        # Get the title form the query
        title = request.query_params.get('title', '')
        
        if title:
            hotel = Hotel.objects.filter(name__icontains = title)
            
        else:
            hotel = Hotel.objects.all()
            

        serializer = HotelSerializer(hotel, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)











class TourAgencyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourAgency.objects.all()
    serializer_class = TourAgencySerializer
    lookup_field = 'pk'


class TourAgencyListCreate(generics.ListCreateAPIView):
    queryset = TourAgency.objects.all()
    serializer_class = TourAgencySerializer
    def get(self, request, format=None):
        # Get the title form the query
        title = request.query_params.get('title', '')
        
        if title:
            agency = TourAgency.objects.filter(name__icontains = title)
            
        else:
            agency = TourAgency.objects.all()
            

        serializer = TourAgencySerializer(agency, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)






class RoomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'pk2'

class RoomList(APIView):
    def get(self, request, format=None):
        # Get the title form the query
        title = request.query_params.get('title', '')
        
        if title:
            room = Room.objects.filter(hotel__name__icontains = title)
            
        else:
            room = Room.objects.all()
            

        serializer = RoomSerializer(room, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)




class VRListCreate(generics.ListCreateAPIView):
    queryset = VRExperience.objects.all()
    serializer_class = VRSerializer
    
    
class VRRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VRExperience.objects.all()
    serializer_class = VRSerializer
    lookup_field = 'pk'
    


class VRList(APIView):
    def get(self, request, format=None):
        # Get the title form the query
        title = request.query_params.get('title', '')
        
        if title:
            vr = VRExperience.objects.filter(title__icontains = title)
            
        else:
            vr = VRExperience.objects.all()
            

        serializer = VRSerializer(vr, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


# class VRRatingListCreate(generics.ListCreateAPIView):
#     queryset = VRRating.objects.all()
#     serializer_class = VRSerializer
    







@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/vrs',
        'GET /api/vrs/:id',
        'GET /api/hotels',
        'GET /api/hotels/:id',
        'GET /api/tours',
        'GET /api/tour/:id',
        'GET /api/agencies',
        'GET /api/agencies/:id',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/users',
        'GET /api/users/:id',
        'POST /api/register/',
        'POST /api/login/',
        'POST /api/edit-profile/',
        'GET /api/edit-profile/',
        'GET /api/logout/',
    ]
    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    users = UserAccount.objects.all()
    serialized = UserAccountSerializer(users, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(username=pk)
    user = UserAccount.objects.get(user=user.id)
    serialized = UserAccountSerializer(user)
    return Response(serialized.data)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("Hello, world!")


@api_view(['POST'])
def editProfile(request):
    user = User.objects.get(username=request.user.username)
    user = UserAccount.objects.get(user=user.id)
    serializer = UserAccountSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getVRs(request):
    vrs = VRExperience.objects.all()
    serialized = VRSerializer(vrs, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getVR(request, pk):
    vr = VRExperience.objects.get(title=pk)
    serialized = VRSerializer(vr)
    return Response(serialized.data)

@api_view(['GET'])
def getHotels(request):
    hotels = Hotel.objects.all()
    serialized = HotelSerializer(hotels, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getHotel(request, pk):
    hotel = Hotel.objects.get(name = pk)
    print(hotel)
    serialized = HotelSerializer(hotel, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getTours(request):
    tours = TourAgency.objects.all()
    serialized = TourAgencySerializer(tours, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getTour(request, pk):
    tour = TourAgency.objects.get(name = pk)
    print(tour)
    serialized = TourAgencySerializer(tour, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getAgencies(request):
    agencies = TourAgency.objects.all()
    serialized = TourAgencySerializer(agencies, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getAgency(request, pk):
    agency = TourAgency.objects.get(name = pk)
    print(agency)
    serialized = TourAgencySerializer(agency, many=True)
    return Response(serialized.data)


#implement login functionality using api

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    token , created= Token.objects.get_or_create(user=user )
    serializer = UserSerializer(instance=user)
    return Response({"token":token.key, "user":serializer.data})

@api_view(['POST'])
def register(request):
    # data = json.loads(request.body)
    # username = data['username']
    # password = data['password']
    # #if username and password
    # user = User.objects.get(username=username)
    # if user.check_password(password):
    #     serialized = UserAccountSerializer(user)
    #     return Response(serialized.data)
    # else:
    #     return Response("Invalid Credentials")
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key, "user":serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def test_token(request):
    # data = json.loads(request.body)
    # username = data['username']
    # password = data['password']
    # #if username and password
    # user = User.objects.get(username=username)
    # if user.check_password(password):
    #     serialized = UserAccountSerializer(user)
    #     return Response(serialized.data)
    # else:
    #     return Response("Invalid Credentials")
    
    return Response({})


