from django.urls import path
from . import  views

urlpatterns = [
    path('', views.vr_experiences, name='vrs'),
    path('vr/<str:pk>/', views.vr_experience, name='vr'),
    path('create-vr/', views.createVR, name='create-vr'),
    path('update-vr/<str:pk>/', views.updateVR, name='update-vr'),
]