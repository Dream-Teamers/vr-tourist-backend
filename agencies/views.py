from .models import Tour, TourAgency, TourBooking, TourRating
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import TourForm, RatingForm
from .models import Tour, Tag, TourRating
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import TourBookingForm, TourForm, RatingForm
from .models import Tour, Tag, TourBooking
from django.contrib.auth.models import User
from users.forms import HelpSupportForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
def tours(request):
    tours = Tour.objects.all()
    message = "Tour Experience"
    
    context = {
        'tours': tours,
        'message': message,
        'rating_range': list(range(1,6)),

    }
    return render(request, 'agencies/vrss.html', context)

def tour(request, pk):
    vrObj = Tour.objects.get(title=pk)
    form = RatingForm()
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours')
    return render(request, 'agencies/single-tour.html', {'tour': vrObj,'rating_range': list(range(1,6)), 'form': form})

def createTour(request):
    form = TourForm()
    if request.method == "POST":
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours')
    context = {
        'form': form
    }
    return render(request, 'agencies/vr_form.html', context)


def updateTour(request, title):
    tour = Tour.objects.get(title=title)
    form = TourForm(instance= tour)
    if request.method == "POST":
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tours')
    context = {
        'form': form
    }
    return render(request, 'agencies/vr_form.html', context)

def deleteTour(request, title):
    tour = Tour.objects.get(title=title)
    
    if request.method == "POST":
        tour.delete()
        return redirect('tours')
    
    context = {
        'tour': tour
    }
    return render(request, 'agencies/delete-tour.html', context)


def rateTour(request, title):
    tour = get_object_or_404(Tour, title=title)
    user = request.user

    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.tour = tour
            rating.user = user
            rating.save()
            return redirect('tours')  # Or redirect to a page showing the Tour experience details
    else:
        form = RatingForm()

    context = {
        'form': form,
        'tour': tour
    }
    return render(request, 'agencies/rate-tour.html', context)

@login_required(login_url='login')
def help_support(request):
    if request.method == 'POST':
        form = HelpSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('help-support')
    else:
        form = HelpSupportForm()
    return render(request, 'agencies/help_support.html', {'form': form})

def bookTour(request, pk):
    tour = get_object_or_404(Tour, title=pk)
    user = User.objects.get(username=request.user.username)
    print(user)
    # if TourBooking.objects.filter(user=request.user, tour=tour).exists():
    #     messages.warning(request, 'You have already booked this Tour experience.')
    # else:
    #     TourBooking.objects.create(user=request.user, tour=tour)
    #     messages.success(request, 'Successfully booked the Tour experience!')
    booking = TourBooking.objects.create(user=user, tour=tour)
    
    return redirect('tours')