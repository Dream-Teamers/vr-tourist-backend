from django.urls import path
from . import  views

urlpatterns = [
    path('vrs/', views.vr_experiences, name='vrs'),
    path('vr/<str:pk>/', views.vr_experience, name='single-vr'),
    path('create-vr/', views.createVR, name='create-vr'),
    path('update-vr/<str:title>/', views.updateVR, name='update-vr'),
    path('book-vr/<str:pk>/', views.book_vr_experience, name='book_vr_experience'),
]