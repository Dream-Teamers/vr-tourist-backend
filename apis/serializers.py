from rest_framework.serializers import ModelSerializer

from vr_experience.models import VRExperience, VRRating
from hotels.models import Hotel, Room
from agencies.models import TourAgency
from users.models import UserAccount
from django.contrib.auth.models import User
from .models import RoomImage, Room, Hotel

class VRSerializer(ModelSerializer):
    class Meta:
        model = VRExperience
        fields = '__all__'
        
class RoomImageSerializer(ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['image_url']


class RoomSerializer(ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_type', 'occupancy', 'price_per_night', 'availability', 'images']


class HotelSerializer(ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['name', 'address', 'description', 'rating', 'amenities', 'price_per_night', 'rooms']
        
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            
        )
        UserAccount.objects.create(user=user, role='role')
        return user
        
class UserAccountSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserAccount
        fields = ['user', 'bio', 'date_of_birth', 'phone_number']
   
