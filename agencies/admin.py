from django.contrib import admin

# Register your models here.
from .models import Tour, TourAgency, TourBooking, TourRating, Tag

admin.site.register(Tour)
admin.site.register(TourAgency)
admin.site.register(TourBooking)
admin.site.register(TourRating)
admin.site.register(Tag)