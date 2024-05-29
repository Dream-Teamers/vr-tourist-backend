from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import VRForm, RatingForm
from .models import VRExperience, Tag, VRRating
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import VRBookingForm, VRForm, RatingForm
from .models import VRExperience, Tag, VRBooking
from django.contrib.auth.models import User

def vr_experiences(request):
    vrs = VRExperience.objects.all()
    message = "VR Experience"
    
    context = {
        'vrs': vrs,
        'message': message,
        'rating_range': list(range(1,6)),

    }
    return render(request, 'vr_experience/vrss.html', context)

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

def deleteVR(request, title):
    vr = VRExperience.objects.get(title=title)
    
    if request.method == "POST":
        vr.delete()
        return redirect('vrs')
    
    context = {
        'vr': vr
    }
    return render(request, 'vr_experience/delete-vr.html', context)


def rateVR(request, title):
    vr_experience = get_object_or_404(VRExperience, title=title)
    user = request.user

    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.vr_experience = vr_experience
            rating.user = user
            rating.save()
            return redirect('vrs')  # Or redirect to a page showing the VR experience details
    else:
        form = RatingForm()

    context = {
        'form': form,
        'vr_experience': vr_experience
    }
    return render(request, 'vr_experience/rate-vr.html', context)



def book_vr_experience(request, pk):
    vr_experience = get_object_or_404(VRExperience, title=pk)
    user = User.objects.get(username=request.user.username)
    print(user)
    # if VRBooking.objects.filter(user=request.user, vr_experience=vr_experience).exists():
    #     messages.warning(request, 'You have already booked this VR experience.')
    # else:
    #     VRBooking.objects.create(user=request.user, vr_experience=vr_experience)
    #     messages.success(request, 'Successfully booked the VR experience!')
    booking = VRBooking.objects.create(user=user, vr_experience=vr_experience)
    
    return redirect('vrs')