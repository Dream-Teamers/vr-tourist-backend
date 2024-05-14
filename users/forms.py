from django.forms import ModelForm
from .models import UserProfile
import logging



# class UserForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
# # complete fields that are required for this model
# and_required = ['email', 'first_name', 'last_name']

# class UserProfileForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'profile_picture']
#         # fields = '__all__'
        
