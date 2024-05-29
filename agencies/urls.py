from django.urls import path
from . import  views

urlpatterns = [
    path('agencies/', views.agenciesPage, name='agencies'),
    path('agency/<str:pk>/', views.agencyPage, name='single-agency'),
    path('profiles/edit/<str:username>/', views.editProfile, name="edit-profile"),
    path('dashboard/agencies/', views.tour_agency_dashboard, name="tour-agency-dashboard"),
    path('add-package-listing/', views.add_tour_package, name="add-tour-package"),
    path('update-tour-package/', views.update_tour_package, name="update-tour-package"),
    path('view-tour-package/', views.view_tour_package, name="view-tour-package"),
    path('manage-package-reviews/', views.manage_tour_reviews, name="manage-package-reviews"),
    # path('add-agencie/', views.createVR, name='add-agencie'),
    # path('update-agencie/<str:title>/', views.updateVR, name='update-agencie'),
]