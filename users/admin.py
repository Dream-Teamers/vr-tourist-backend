from django.contrib import admin
from .models import UserProfile, ActivityLog, PaymentMethod, Wishlist, Address, UserAccount
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ActivityLog)
admin.site.register(PaymentMethod)
admin.site.register(Wishlist)
admin.site.register(Address)
admin.site.register(UserAccount)