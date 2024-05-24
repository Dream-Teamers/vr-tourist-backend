from rest_framework.decorators import api_view
from rest_framework.response import Response
from vr_experience.models import VRExperience
from hotels.models import Hotel
from agencies.models import TourAgency
from users.models import UserAccount
from .serializers import VRSerializer, HotelSerializer
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