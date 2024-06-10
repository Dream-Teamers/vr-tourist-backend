from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    
    
    
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('test_token/', views.test_token),
    # login path
    
    #path('login/', views.login)
    path('vrs/', views.VRListCreate.as_view(), name='vr-view-create'),
    path('vrs/rating/<int:pk>/', views.VRRetrieveUpdateDestroy.as_view(), name='vr-rating'),
    path('vrs/<int:pk>/', views.VRRetrieveUpdateDestroy.as_view(), name='vr-update'),
    path('vrs/bookings/', views.VRBookingListCreate.as_view(), name='vr-booking-view-create'),
    
    # path for agencies
    path('agencies/', views.TourAgencyListCreate.as_view(), name='agency-view-create'),
    path('agencies/<int:pk>/', views.TourAgencyRetrieveUpdateDestroy.as_view(), name='agency-update'),
    
    # path for tours
    path('tours/', views.TourListCreate.as_view(), name='tour-view-create'),
    path('tours/<int:pk>/', views.TourRetrieveUpdateDestroy.as_view(), name='tour-update'),
    # path for tour bookings
    path('tours/bookings/', views.TourBookingListCreate.as_view(), name='tour-booking'),
    
    
    # path('vrs/<int:pk>/book/', views.VRBookingRetrieveUpdateDestroy.as_view(), name='vr-booking'),
    
    
    
    path('ratings/', views.VRRatingListCreate.as_view(), name='vr-rating-view-create'),
    
    path('mybookings/', views.listBookings, name='my-bookings'),
    
    # user profile path
    path('profiles/', views.ProfileListCreate.as_view(), name='profile-view-create'),
    path('profiles/<int:pk>/', views.ProfileRetrieveUpdateDestroy.as_view(), name='profile-update'),
    # path('agencies/', views.TourAgencyListCreate.as_view(), name='agency-view-create'),
    # path('agencies/<int:pk>/', views.TourAgencyRetrieveUpdateDestroy.as_view(), name='agency-update'),
    
    
    # path('tours/', views.getTours),
    # path('tour/<str:pk>/', views.getTour),
    

    
    path('hotels/', views.HotelListCreate.as_view(), name ='hotel-view-create'),
    path('hotels/<int:pk>/', views.HotelRetrieveUpdateDestroy.as_view(), name ='hotel-update'),
    
    
    
    path('rooms/', views.RoomListCreate.as_view(), name ='hotel-view-create'),
    path('rooms/<int:pk>/', views.RoomRetrieveUpdateDestroy.as_view(), name ='hotel-update'),
    
    
    
    path('users/', views.ProfileListCreate.as_view(), name='profile-view-create'),
    path('users/<str:pk>/', views.ProfileRetrieveUpdateDestroy.as_view(), name='profile-update'),
    
]