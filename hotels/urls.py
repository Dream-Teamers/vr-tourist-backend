from django.urls import path
from . import  views

urlpatterns = [
    path('hotels/', views.hotelsPage, name='hotels'),
    path('hotel/<str:pk>/', views.hotelPage, name='single-hotel'),
    path('dashboard/', views.hotel_manager_dashboard, name="hotel-manager-dashboard"),
    
    path('dashboard/', views.hotel_manager_dashboard, name="hotel-manager-dashboard"),
    path('add-hotel-listing/', views.add_hotel_listing, name="add-hotel-listing"),
    path('update-hotel-listing/', views.update_hotel_listing, name="update-hotel-listing"),
    path('delete-hotel-listing/', views.delete_hotel_listing, name="delete-hotel-listing"),
    path('view-hotel-bookings/', views.view_hotel_bookings, name="view-hotel-bookings"),
    path('manage-hotel-reviews/', views.manage_hotel_reviews, name="manage-hotel-reviews"),
]




    # path('add-hotel/', views.createVR, name='add-hotel'),
    # path('update-hotel/<str:title>/', views.updateVR, name='update-hotel'),
