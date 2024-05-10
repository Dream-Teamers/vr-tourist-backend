from django.contrib import admin

# Register your models here.
from .models import VRExperience, Tag, VRReview

admin.site.register(VRExperience)
admin.site.register(Tag)
admin.site.register(VRReview)
