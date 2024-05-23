from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('vrs/', views.getVRs),
    path('vr/<str:pk>/', views.getVR),
    path('hotels/', views.getHotels),
]