from django.forms import ModelForm
from .models import VRExperience, VRRating, VRBooking, VRBooking
from django import forms

class VRForm(ModelForm):
    class Meta:
        model = VRExperience
        fields = ['title','description','price'] 

        
class RatingForm(ModelForm):
    class Meta:
        model = VRRating
        fields = ['value','comment']

class VRBookingForm(forms.ModelForm):
    class Meta:
        model = VRBooking
        fields = ['user','vr_experience']
