from rest_framework.decorators import api_view
from rest_framework.response import Response
from vr_experience.models import VRExperience
from hotels.models import Hotel
from agencies.models import TourAgency
from django.contrib.auth.models import User
from users.models import UserAccount
from .serializers import VRSerializer, HotelSerializer, TourAgencySerializer, UserAccountSerializer, UserSerializer
import json


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/vrs',
        'GET /api/vr/:id',
        'GET /api/hotels',
        'GET /api/hotel/:id',
        'GET /api/tours',
        'GET /api/tour/:id',
        'GET /api/agencies',
        'GET /api/agency/:id',
        'GET /api/rooms',
        'GET /api/room/:id',
        'GET /api/users',
        'GET /api/user/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    users = UserAccount.objects.all()
    serialized = UserAccountSerializer(users, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def getUser(request, pk):
    user = UserAccount.objects.get(user=pk)
    serialized = UserAccountSerializer(user)
    return Response(serialized.data)


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
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    #if username and password
    user = User.objects.get(username=username)
    if user.check_password(password):
        serialized = UserAccountSerializer(user)
        return Response(serialized.data)
    else:
        return Response("Invalid Credentials")
    