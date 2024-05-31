from django.forms import ModelForm
from .models import Tour, TourRating, TourBooking, TourBooking
from django import forms

class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['title','description','price'] 

        
class RatingForm(forms.ModelForm):
    class Meta:
        model = TourRating
        fields = ['value', 'comment']
        widgets = {
            'value': forms.RadioSelect(choices=TourRating.VOTE_TYPE),
        }

class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ['user','tour']
