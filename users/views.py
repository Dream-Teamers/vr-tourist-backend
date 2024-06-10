from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from apis.serializers import UserSerializer, UserAccountSerializer
from django.contrib.auth.models import User
from .models import UserAccount
from vrs.models import VRBooking
from apis.serializers import VRBookingSerializer
from apis.permissions import IsAuthenticatedOrReadOnly, IsAdminUser




@api_view(['POST','GET'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    useraccount = get_object_or_404(UserAccount, user=user)
    print(useraccount.role)
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    user_account = useraccount
    token , created= Token.objects.get_or_create(user=user )
    serializer = UserSerializer(instance=user)
    if user_account.role == 'tourist':
        return Response({"token":token.key, "user":serializer.data, "role":"tourist"})
    elif user_account.role == 'tour_agency':
        return Response({"token":token.key, "user":serializer.data, "role":"agency"})
    elif user_account.role == 'admin':
        return Response({"token":token.key, "user":serializer.data, "role":"admin"})
    elif user_account.role == 'hotel':
       return Response({"token":token.key, "user":serializer.data, "role":"hotel"})
    else:
        return Response({"token":token.key, "user":serializer.data, "role":"guest"})
    # return Response({"message": "Hello"})

@api_view(['POST'])
def register(request):
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
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))

## logout view for the user
@api_view(['POST'])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"message": "You were Logged out"})
# list user bookings
@api_view(['GET'])
def listBookings(request):
    serializer = VRBookingSerializer(VRBooking.objects.filter(user=request.user.id), many=True)
    print(request.user.id)
    print(serializer.data)
    return Response(serializer.data)   



## user profile view
@api_view(['GET'])
def userProfile(request,username):
    user = User.objects.get(username=username)
    useraccount = get_object_or_404(UserAccount, user=user.id)
    serializer = UserSerializer(instance=user)
    return Response({"user":serializer.data, "role":useraccount.role})


class ProfileListCreate(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    
## permissions.py code for IsAdminUser
# from rest_framework.permissions import BasePermission

# class IsAdminUser(BasePermission):
#     """
#     Custom permission to allow only admin users to access the view.
#     """

#     def has_permission(self, request, view):
#         return request.user and request.user.is_authenticated and request.user.useraccount.role == 'admin'


class ProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'pk'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
## a view that lists users which have a role of spesific role in the params
