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

