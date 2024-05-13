from django.forms import ModelForm
from .models import UserProfile



class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

# Check if the user is authenticated
        def is_authenticated(self , user):
            return user.is_authenticated
        