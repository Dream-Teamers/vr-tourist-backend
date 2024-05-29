from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from users.forms import UserUpdateForm, HelpSupportForm
from .forms import CustomUserCreationForm
from .models import UserAccount




def registerPage(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = form.save(commit=False)
                user.username = username
                user.save()
                
                # Create UserAccount instance with selected role
                if not UserAccount.objects.filter(user=user).exists():

                    role = form.cleaned_data.get('role', 'tourist')
                    UserAccount.objects.create(user=user, role=role)
                    
                messages.success(request, 'Account was created. Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')

    return render(request, 'users/register.html', {'form': form})



def loginUser(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')
            return redirect('login')

        # except:
        #     messages.error(request, 'Username does not exist')
            

        user = authenticate(username=username, password=password)

        if user is not None:
            
            login(request, user)
            user_account = request.user.useraccount
            # next_url = request.GET.get('next', 'home')
            if user_account.role == 'tourist':
                return redirect('home')
            elif user_account.role == 'tour_agency':
                return redirect('tour-agency-dashboard')
            elif user_account.role == 'admin':
                return redirect('admin-dashboard')
            elif user_account.role == 'hotel':
                return redirect('hotel-manager-dashboard')
            else:
                return redirect('vrs')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')



@login_required(login_url='login')
def tourist_dashboard(request):
    return render(request, 'users/tourist_dashboard.html')

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')




@login_required(login_url='login')
def userProfile(request, username):
    # profile = get_object_or_404(UserProfile, username=username)
    profile = get_object_or_404(User, username=username)
    context = {'profile': profile,}
    return render(request, 'users/profiles.html', context)


@login_required(login_url='login')
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
    return render(request, 'users/edit_profile.html', context)



@login_required(login_url='login')
def book_tour(request):
    return render(request, 'users/book_tour.html')

@login_required(login_url='login')
def my_tours(request):
    return render(request, 'users/my_tours.html')

@login_required(login_url='login')
def explore_tours(request):
    return render(request, 'users/explore_tours.html')

@login_required(login_url='login')
def account_settings(request):
    return render(request, 'users/account_settings.html')

@login_required(login_url='login')
def notifications(request):
    return render(request, 'users/notifications.html')

@login_required(login_url='login')
def help_support(request):
    if request.method == 'POST':
        form = HelpSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('help-support')
    else:
        form = HelpSupportForm()
    return render(request, 'users/help_support.html', {'form': form})

    #return render(request, 'users/help_support.html')

@login_required(login_url='login')
def settings(request):
    return render(request, 'users/settings.html')


# Role based dashboard
@login_required(login_url='login')
def role_dashboard(request, role):
    if role == 'tourist':
        return redirect('tourist-dashboard')
    elif role == 'tour_agency':
        return redirect('tour-agency-dashboard')
    elif role == 'hotel':
        return redirect('hotel-manager-dashboard')
    else:
        return redirect('home')






@login_required(login_url='login')
def home(request):
    user_account = request.user.useraccount
    context = {
        'user_role': user_account.role
    }
    return render(request, 'users/home.html', context)















