from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def get_homepage(request):
    return redirect(request,'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vr_experience.urls')),
    path('', include('users.urls')),
    path('', include('hotels.urls')),
    path('', include('agencies.urls')),
    path('api/', include('apis.urls')),
    path('accounts/', include('allauth.urls')),
    

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)