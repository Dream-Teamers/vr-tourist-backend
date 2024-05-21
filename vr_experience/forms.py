from django.forms import ModelForm
from .models import VRExperience, VRRating


class VRForm(ModelForm):
    class Meta:
        model = VRExperience
        fields = ['title','description','duration','price'] 

        
class RatingForm(ModelForm):
    class Meta:
        model = VRRating
        fields = ['value','comment']