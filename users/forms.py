from django.forms import ModelForm
from .models import UserProfile
import logging



class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
