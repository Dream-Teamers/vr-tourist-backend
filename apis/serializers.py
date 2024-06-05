from rest_framework.serializers import ModelSerializer

from vr_experience.models import VRExperience, VRRating
from hotels.models import Hotel, Room
from agencies.models import TourAgency
from users.models import UserAccount
from django.contrib.auth.models import User




        
class TourAgencySerializer(ModelSerializer):
    class Meta:
        model = TourAgency
        fields = ['id','name', 'description',  'image_url']



class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','hotel', 'room_type', 'occupancy', 'price_per_night', 'availability']



class HotelSerializer(ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['id','name', 'description', 'locations', 'image_url', 'rooms']


class VRSerializer(ModelSerializer):
    class Meta:
        model = VRExperience
        fields = ['id', 'title', 'description','price']
        
        
class VRRatingSerializer(ModelSerializer):
    class Meta:
        model = VRRating
        fields = '__all__'
        
        
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
   
