from django.contrib import admin

# Register your models here.
from .models import VRExperience, Tag, VRRating, VRBooking, VRBooking

admin.site.register(VRExperience)
admin.site.register(Tag)
admin.site.register(VRRating)
admin.site.register(VRBooking)

