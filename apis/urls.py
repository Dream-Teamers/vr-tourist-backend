from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.getRoutes),
    # path('vrs/', views.getVRs),
    # path('vr/<str:pk>/', views.getVR),

    
    
    path('agencies/', views.TourAgencyListCreate.as_view(), name='agency-view-create'),
    path('agencies/<int:pk>/', views.TourAgencyRetrieveUpdateDestroy.as_view(), name='agency-update'),
    
    
    path('tours/', views.getTours),
    path('tour/<str:pk>/', views.getTour),
    

    
    path('hotels/', views.HotelListCreate.as_view(), name ='hotel-view-create'),
    path('hotels/<int:pk>/', views.HotelRetrieveUpdateDestroy.as_view(), name ='hotel-update'),
    
    
    
    path('rooms/', views.RoomList.as_view(), name ='hotel-view-create'),
    path('rooms/<int:pk>/', views.RoomRetrieveUpdateDestroy.as_view(), name ='hotel-update'),
    
    
    
    path('users/', views.getUsers),
    path('user/<str:pk>/', views.getUser),
    
    
    path('register/', views.register),
    path('login/', views.login),
    path('test_token/', views.test_token),
    # login path
    
    #path('login/', views.login)
    path('vrs/', views.VRListCreate.as_view(), name='vr-view-create'),
    path('vrs/rating/<int:pk>/', views.VRRetrieveUpdateDestroy.as_view(), name='vr-rating'),
    path('vrs/<int:pk>/', views.VRRetrieveUpdateDestroy.as_view(), name='vr-update'),
]