from django.contrib import admin

# Register your models here.
from .models import Tour, TourAgency, TourImage, TourReview, TourBooking

admin.site.register(Tour)
admin.site.register(TourAgency)
admin.site.register(TourImage)
admin.site.register(TourReview)
admin.site.register(TourBooking)