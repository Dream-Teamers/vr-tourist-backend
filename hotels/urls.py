from django.urls import path
from . import  views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('hotels/', views.hotelsPage, name='hotels'),
    # path('hotel/<str:pk>/', views.hotelPage, name='single-hotel'),
    # path('dashboard/', views.hotel_manager_dashboard, name="hotel-manager-dashboard"),
    
    path('hotels/', views.hotelsPage, name='hotels'),
    path('hotel/<str:pk>/', views.hotelPage, name='single-hotel'),
    path('dashboard/', views.hotel_manager_dashboard, name="hotel-manager-dashboard"),
    path('add-hotel-listing/', views.add_hotel_listing, name="add-hotel-listing"),
    path('update-hotel-listing/<int:pk>/', views.update_hotel_listing, name="update-hotel-listing"),
    path('delete-hotel-listing/<str:pk>/', views.delete_hotel_listing, name="delete-hotel-listing"),
    path('view-hotel-bookings/', views.view_hotel_bookings, name="view-hotel-bookings"),
    path('manage-hotel-reviews/', views.manage_hotel_reviews, name="manage-hotel-reviews"),



    path('rooms/<int:hotel_id>/', views.room_list, name='room_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('add-room/<int:pk>/', views.room_add, name='room_add'),
    path('rooms/<int:pk>/update/', views.room_update, name='room_update'),
    # path('rooms/<int:pk>/delete/', views.room_delete, name='room_delete'),
    path('rooms/<int:pk>/check-availability/', views.check_room_availability, name='check_room_availability'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('rooms/create/<int:pk>/', views.room_add, name='room_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




    # path('add-hotel/', views.createVR, name='add-hotel'),
    # path('update-hotel/<str:title>/', views.updateVR, name='update-hotel'),
