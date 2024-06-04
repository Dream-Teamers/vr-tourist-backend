from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import HelpSupport
from users.models import UserProfile, UserAccount


class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('tourist', 'Tourist'),
        ('tour_agency', 'Tour Agent'),
        ('hotel', 'Hotel Manager'),
    )
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=False, initial='tourist')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class UserAccountUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['date_of_birth', 'phone_number', 'bio']
        
        
class HelpSupportForm(forms.ModelForm):
    class Meta:
        model = HelpSupport
        fields = ['name', 'email', 'question']




























# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('profile_picture', 'bio', 'date_of_birth', 'contact_info')
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('username', 'password', 'password_confirmation')