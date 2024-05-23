from rest_framework.serializers import ModelSerializer
from vr_experience.models import VRExperience
from hotels.models import Hotel
from agencies.models import TourAgency
from users.models import UserAccount

class VRSerializer(ModelSerializer):
    class Meta:
        model = VRExperience
        fields = '__all__'
        
class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'