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

def vr_experience(request, pk):
    vrObj = VRExperience.objects.get(title=pk)
    form = RatingForm()
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vrs')
    return render(request, 'vr_experience/single-vr.html', {'vr': vrObj,'rating_range': list(range(1,6)), 'form': form})

def createVR(request):
    form = VRForm()
    if request.method == "POST":
        form = VRForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vrs')
    context = {
        'form': form
    }
    return render(request, 'vr_experience/vr_form.html', context)


def updateVR(request, title):
    vr = VRExperience.objects.get(title=title)
    form = VRForm(instance= vr)
    if request.method == "POST":
        form = VRForm(request.POST, instance=vr)
        if form.is_valid():
            form.save()
            return redirect('vrs')
    context = {
        'form': form
    }
    return render(request, 'vr_experience/vr_form.html', context)