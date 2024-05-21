from django.urls import path
from . import  views

urlpatterns = [
    path('hotels/', views.hotelsPage, name='hotels'),
    path('hotel/<str:pk>/', views.hotelPage, name='single-hotel'),
    # path('add-hotel/', views.createVR, name='add-hotel'),
    # path('update-hotel/<str:title>/', views.updateVR, name='update-hotel'),
]