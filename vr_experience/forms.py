from django.forms import ModelForm
from .models import VRExperience
import logging



class VRForm(ModelForm):
    class Meta:
        model = VRExperience
        fields = ['title','description','duration','price'] 
