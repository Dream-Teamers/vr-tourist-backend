from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import VRForm, RatingForm
from .models import Hotel, Room, RoomReview, RoomBooking

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

