from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import VRForm, RatingForm
from .models import Tour, TourAgency, TourBooking, TourReview
from django.contrib.auth.decorators import login_required
from users.forms import UserUpdateForm, HelpSupportForm
from django.contrib import messages
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

@login_required(login_url='login')
def tour_agency_dashboard(request):
    return render(request, 'agencies/tour_agency_dashboard.html')

@login_required(login_url='login')
def add_tour_package(request):
    # Implement functionality to add hotel listing
    return render(request, 'agencies/add_tour_package.html')

@login_required(login_url='login')
def update_tour_package(request):
    # Implement functionality to update hotel listing
    return render(request, 'agencies/update_tour_package.html')

@login_required(login_url='login')
def view_tour_package(request):
    # Implement functionality to delete hotel listing
    return render(request, 'agencies/view_tour_package.html')

@login_required(login_url='login')
def manage_tour_reviews(request):
    # Implement functionality to view hotel bookings
    return render(request, 'agencies/manage_tour_reviews.html')


@login_required(login_url='login')
def notifications(request):
    return render(request, 'agencies/notifications.html')

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

def editProfile(request, username):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('user-profile', username=request.user.username)
    else:
        form = UserUpdateForm(instance=request.user)

    context = {'form': form}
    return render(request, 'agencies/edit_profile.html', context)