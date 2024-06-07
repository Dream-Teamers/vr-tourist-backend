from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('test/', views.test_token, name='test'),
    # path('profile/', views.profile, name='profile'),
]