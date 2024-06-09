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
    
    
class ProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    lookup_field = 'pk'
    
## a view that lists users which have a role of spesific role in the params
@api_view(['GET'])
def getUsers(request, role):
    users = UserAccount.objects.filter(role=role)
    serializer = UserAccountSerializer(users, many=True)
    return Response(serializer.data)
### url path for the above view
# path('users/<str:role>/', views.getUsers),
## any necessary changes to the serializers
# class UserAccountSerializer(ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = UserAccount
#         fields = ['id', 'user', 'bio', 'date_of_birth', 'phone_number']
# any necessary changes to the whole system because of the above getUsers view
# no changes needed
## a view that returns all users
@api_view(['GET'])
def getUsers(request):
    users = UserAccount.objects.all()
    serializer = UserAccountSerializer(users, many=True)
    return Response(serializer.data)