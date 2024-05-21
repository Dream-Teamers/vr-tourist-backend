from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import VRForm, RatingForm
from .models import Tour, TourAgency, TourBooking, TourReview

def agenciesPage(request):
    agencies = TourAgency.objects.all()
    message = "Agencies"
    context = {
        'agencies': agencies,
        'message': message,
        'rating_range': list(range(1,6)),

    }
    return render(request, 'agencies/agencies.html', context)
def agencyPage(request,pk):
    agency = TourAgency.objects.get(name=pk)
    message = "Agency"
    context = {
        'agency': agency,
        'message': message,
        'rating_range': list(range(1,6)),

    }
    return render(request, 'agencies/single-agency.html', context)

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