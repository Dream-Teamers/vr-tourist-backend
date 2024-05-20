from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VRForm
from .models import VRExperience

def vr_experiences(request):
    vrs = VRExperience.objects.all()
    message = "VR Experience"
    context = {
        'vrs': vrs,
        'message': message,
        'rating_range': list(range(1,6))
    }
    return render(request, 'vr_experience/vrss.html', context)

def vr_experience(request, pk):
    vrObj = VRExperience.objects.get(title=pk)
    return render(request, 'vr_experience/single-vr.html', {'vr': vrObj,'rating_range': list(range(1,6))})

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