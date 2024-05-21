from django.urls import path
from . import  views

urlpatterns = [
    path('agencies/', views.agenciesPage, name='agencies'),
    path('agency/<str:pk>/', views.agencyPage, name='single-agency'),
    # path('add-agencie/', views.createVR, name='add-agencie'),
    # path('update-agencie/<str:title>/', views.updateVR, name='update-agencie'),
]