from django.contrib import admin

# Register your models here.
from .models import VRExperience, Tag, VRRating

admin.site.register(VRExperience)
admin.site.register(Tag)
admin.site.register(VRRating)
