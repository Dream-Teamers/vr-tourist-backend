from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    # path('account/', views.userAccount, name="account"),

    path('edit-account/', views.editAccount, name="edit-account"),

    # path('create-role/', views.createrole, name="create-role"),
    # path('update-role/<str:pk>/', views.updaterole, name="update-role"),
    # path('delete-role/<str:pk>/', views.deleterole, name="delete-role"),

    # path('inbox/', views.inbox, name="inbox"),
    # path('message/<str:pk>/', views.viewMessage, name="message"),
    # path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]
