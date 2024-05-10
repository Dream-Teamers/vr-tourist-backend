from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VRForm
from .models import VRExperience

def vr_experiences(request):
    page = "VR Experience"
    return render(request, 'vr_experience/vrs.html', {'message':page})

def vr_experience(request, pk):
    return render(request, 'vr_experience/single-vr.html')

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

def updateVR(request, pk):
    vr = VRExperience.objects.get(id=pk)
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