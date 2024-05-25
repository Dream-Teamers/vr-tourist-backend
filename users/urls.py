from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    #path('', views.profiles, name="profiles"),
    path('profiles/<str:username>/', views.userProfile, name="user-profile"),
    path('home/', views.home, name="home"),
    path('profiles/edit/<str:username>/', views.editProfile, name="edit-profile"),
    
    #Role based redirection
    # path('role-dashboard/<str:role>/', views.role_dashboard, name="role-dashboard"),
    path('admin-dashboard/', views.admin_dashboard, name="admin"),

    path('book-tour/', views.book_tour, name="book-tour"),
    path('my-tours/', views.my_tours, name="my-tours"),
    path('explore-tours/', views.explore_tours, name="explore-tours"),
    path('account-settings/', views.account_settings, name="account-settings"),
    path('notifications/', views.notifications, name="notifications"),
    path('help-support/', views.help_support, name="help-support"),
    path('settings/', views.settings, name="settings"),


    # path('account/', views.userAccount, name="account"),

    #path('edit-account/', views.editAccount, name="edit-account"),

    # path('create-role/', views.createrole, name="create-role"),
    # path('update-role/<str:pk>/', views.updaterole, name="update-role"),
    # path('delete-role/<str:pk>/', views.deleterole, name="delete-role"),

    # path('inbox/', views.inbox, name="inbox"),
    # path('message/<str:pk>/', views.viewMessage, name="message"),
    # path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]
