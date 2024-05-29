from django.urls import path
from . import  views

urlpatterns = [
    path('', views.vr_experiences, name='vrs'),
    path('vr/<str:pk>/', views.vr_experience, name='single-vr'),
    path('create-vr/', views.createVR, name='create-vr'),
    path('update-vr/<str:title>/', views.updateVR, name='update-vr'),
    path('rate-vr/<str:pk>/', views.rateVR, name='rate-vr'),
    path('delete/<str:title>/', views.deleteVR, name='delete-vr'),
]