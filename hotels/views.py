from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import VRForm, RatingForm
from .models import Hotel, Room, RoomReview, RoomBooking
from django.contrib.auth.decorators import login_required
def hotelsPage(request):
    hotels = Hotel.objects.all()
    message = "Hotels"
    context = {
        'hotels': hotels,
        'message': message,
        'rating_range': list(range(1,6)),

    }
    return render(request, 'hotels/hotels.html', context)
def hotelPage(request,pk):
    hotel = Hotel.objects.get(name=pk)
    message = "Hotel"
    context = {
        'hotel': hotel,
        'message': message,
        'rating_range': list(range(1,6)),

    }
    return render(request, 'hotels/single-hotel.html', context)

@login_required(login_url='login')
def hotel_manager_dashboard(request):
    return render(request, 'hotels/hotel_manager_dashboard.html')



@login_required(login_url='login')
def add_hotel_listing(request):
    # Implement functionality to add hotel listing
    return render(request, 'hotel/add_hotel_listing.html')

@login_required(login_url='login')
def update_hotel_listing(request):
    # Implement functionality to update hotel listing
    return render(request, 'hotel/update_hotel_listing.html')

@login_required(login_url='login')
def delete_hotel_listing(request):
    # Implement functionality to delete hotel listing
    return render(request, 'hotel/delete_hotel_listing.html')

@login_required(login_url='login')
def view_hotel_bookings(request):
    # Implement functionality to view hotel bookings
    return render(request, 'hotel/view_hotel_bookings.html')

@login_required(login_url='login')
def manage_hotel_reviews(request):
    # Implement functionality to manage hotel reviews
    return render(request, 'hotel/manage_hotel_reviews.html')