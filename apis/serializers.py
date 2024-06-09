from rest_framework.serializers import ModelSerializer
from users.models import UserAccount
from django.contrib.auth.models import User
from vrs.models import VR, VRRating, VRBooking
from hotels.models import Hotel, HotelRating, Room, RoomBooking, RoomImage
from agencies.models import AgencyRating, Tour, TourAgency, TourBooking

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
        UserAccount.objects.create(user=user, role='tourist')
        return user
        
class UserAccountSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserAccount
        fields = ['id', 'user', 'bio', 'date_of_birth', 'phone_number', 'role']
        
        
class VRSerializer(ModelSerializer):
    class Meta:
        model = VR
        fields = ['id', 'title', 'description','price', 'tags', 'locations', 'image_url', 'vr_url']
        
        
class VRRatingSerializer(ModelSerializer):
    class Meta:
        model = VRRating
        fields = '__all__'
        
        
# how to create the vr booking serializer class
class VRBookingSerializer(ModelSerializer):
    class Meta:
        model = VRBooking
        fields = '__all__'
        
        
from rest_framework.serializers import ModelSerializer

class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'title', 'description', 'price', 'tags', 'locations', 'image_url', 'tour_url']

class AgencyRatingSerializer(ModelSerializer):
    class Meta:
        model = AgencyRating
        fields = '__all__'

class TourBookingSerializer(ModelSerializer):
    class Meta:
        model = TourBooking
        fields = '__all__'

class TourAgencySerializer(ModelSerializer):
    class Meta:
        model = TourAgency
        fields = ['id', 'name', 'description', 'address', 'contact_info', 'tours']
class RoomImageSerializer(ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'image_url']

class RoomSerializer(ModelSerializer):
    # images = RoomImageSerializer(many=True)
    class Meta:
        model = Room
        fields = ['id','room_type', 'occupancy', 'price_per_night', 'availability', 'images']

class RoomTypeSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','room_type']

class HotelSerializer(ModelSerializer):
    rooms = RoomTypeSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'description', 'rating', 'amenities', 'price_per_night', 'rooms', 'image_url']