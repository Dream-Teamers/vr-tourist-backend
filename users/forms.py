from django.forms import ModelForm
from .models import UserProfile
import logging


<<<<<<< HEAD

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
        
=======
# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super(UserRegistrationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.username = self.cleaned_data['username'].lower()
        
#         if commit:
#             user.save()
#         return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('profile_picture', 'bio', 'date_of_birth', 'contact_info')
class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'password_confirmation')
>>>>>>> ec9081bce7fce8210024c9d11166dfbcb3bb4529
