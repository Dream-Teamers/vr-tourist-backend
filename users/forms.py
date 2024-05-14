from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import UserProfile

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