from django.contrib import admin
from .models import AgencyRating, Tour, TourAgency, TourBooking

# Register your models here.
admin.site.register(AgencyRating)
admin.site.register(Tour)
admin.site.register(TourAgency)
admin.site.register(TourBooking)
