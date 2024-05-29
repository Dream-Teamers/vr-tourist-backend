from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('vrs/', views.getVRs),
    path('vr/<str:pk>/', views.getVR),

    
    
    path('agencies/', views.getAgencies),
    path('agency/<str:pk>/', views.getAgency),
    
    
    path('tours/', views.getTours),
    path('tour/<str:pk>/', views.getTour),
    

    
    path('hotels/', views.getHotels),
    path('hotel/<str:pk>/', views.getHotel),
    
    
    
    path('users/', views.getUsers),
    path('user/<str:pk>/', views.getUser),
    
    
    # login path
    
    path('login/', views.login)
    
]