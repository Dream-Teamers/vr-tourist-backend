from django.forms import ModelForm
from .models import VRExperience


class VRForm(ModelForm):
    class Meta:
        model = VRExperience
        fields = ['title','description','duration','price'] 
