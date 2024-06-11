from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from users.views import *
from hotels.views import *
from agencies.views import *
from vrs.views import *


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/vrs/',
        'GET /api/vrs/:id',
        'GET /api/hotels/',
        'GET /api/hotels/:id',
        'GET /api/tours/',
        'GET /api/tour/:id',
        'GET /api/agencies/',
        'GET /api/agencies/:id',
        'GET /api/rooms/',
        'GET /api/rooms/:id',
        'GET /api/users/',
        'GET /api/users/:id',
        'POST /api/register/',
        'POST /api/login/',
        'POST /api/edit-profile/',
        'GET /api/edit-profile/',
        'GET /api/logout/',
    ]
    return Response(routes)
