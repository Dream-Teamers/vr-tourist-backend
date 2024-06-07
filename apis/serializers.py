from rest_framework.serializers import ModelSerializer
from users.models import UserAccount
from django.contrib.auth.models import User
from vrs.models import VR, VRRating, VRBooking

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
        fields = ['id', 'user', 'bio', 'date_of_birth', 'phone_number']
        
        
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