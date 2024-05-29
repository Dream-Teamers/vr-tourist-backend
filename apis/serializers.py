from rest_framework.serializers import ModelSerializer
from vr_experience.models import VRExperience
from hotels.models import Hotel
from agencies.models import TourAgency
from users.models import UserAccount
from django.contrib.auth.models import User

class VRSerializer(ModelSerializer):
    class Meta:
        model = VRExperience
        fields = '__all__'
        
class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        
class UserAccountSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserAccount
        fields = '__all__' 
        
class TourAgencySerializer(ModelSerializer):
    class Meta:
        model = TourAgency
        fields = '__all__'
