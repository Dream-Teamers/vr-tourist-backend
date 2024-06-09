from rest_framework.serializers import ModelSerializer
from users.models import UserAccount
from django.contrib.auth.models import User
from vrs.models import VR, VRRating, VRBooking
from hotels.models import Hotel, HotelRating, Room, RoomBooking, RoomImage
from agencies.models import AgencyRating, Tour, TourAgency, TourBooking

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',  'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        UserAccount.objects.create(user=user, role='tourist')
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
            instance.save()

        return instance

class UserAccountSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserAccount
        fields = ['id', 'user', 'bio', 'date_of_birth', 'phone_number', 'role']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user_account = UserAccount.objects.create(user=user, **validated_data)
        return user_account

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.bio = validated_data.get('bio', instance.bio)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.role = validated_data.get('role', instance.role)
        instance.save()

        UserSerializer.update(UserSerializer(), instance=user, validated_data=user_data)
        return instance
        
        
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
        

class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'title', 'description', 'duration', 'price', 'locations', 'image_url']

class AgencyRatingSerializer(ModelSerializer):
    class Meta:
        model = AgencyRating
        fields = '__all__'

class TourBookingSerializer(ModelSerializer):
    class Meta:
        model = TourBooking
        fields = '__all__'

class TourAgencySerializer(ModelSerializer):
    tours = TourSerializer(many=True)

    class Meta:
        model = TourAgency
        fields = ['id', 'name', 'description', 'contact_info', 'tours']

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
    rooms = RoomTypeSerializer(many=True)
    class Meta:
        model = Hotel
        fields = ['id', 'admin', 'name', 'address', 'description', 'rating', 'amenities', 'price_per_night', 'rooms', 'image_url']