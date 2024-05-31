from django.urls import path
from . import  views

urlpatterns = [
    path('agencies/', views.agenciesPage, name='agencies'),
    path('agency/<str:pk>/', views.agencyPage, name='single-agency'),
    # path('tours/', views.tour_experiences, name='tours'),
    # path('tour/<str:pk>/', views.tour_experience, name='single-tour'),
    # path('create-tour/', views.createVR, name='create-tour'),
    # path('update-tour/<str:title>/', views.updateVR, name='update-tour'),
    # path('rate-tour/<str:title>/', views.rateVR, name='rate-tour'),
    # path('delete-tour/<str:title>/', views.deleteVR, name='delete-tour'),
    path('book-tour/<str:pk>/', views.bookTour, name='book-tour'),
]