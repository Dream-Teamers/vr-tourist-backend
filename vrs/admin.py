from django.contrib import admin
from .models import VR, VRBooking, VRRating, Tag

# Register your models here.
admin.site.register(VR)
admin.site.register(VRBooking)
admin.site.register(VRRating)
admin.site.register(Tag)