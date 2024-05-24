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



# def registerPage(request):
#     form = CustomUserCreationForm()
    
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             role = form.cleaned_data.get('role', 'tourist')
#             UserAccount.objects.create(user=user, role=role)
            
#             login(request, user)
#             messages.success(request, 'Account was created')
#             return redirect('login')
#         else:
#             messages.error(request, 'Unsuccessful registration. Invalid information.')

#     return render(request, 'users/register.html', {'form': form})
def registerPage(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            role = form.cleaned_data.get('role', 'tourist')
            UserAccount.objects.create(user=user, role=role)
            
            login(request, user)
            messages.success(request, 'Account was created')
            return redirect('role-dashboard', role=role)
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')

    return render(request, 'users/register.html', {'form': form})

#

@login_required(login_url='login')
def tourist_dashboard(request):
    return render(request, 'users/tourist_dashboard.html')

@login_required(login_url='login')
def tour_agency_dashboard(request):
    return render(request, 'users/tour_agency_dashboard.html')

@login_required(login_url='login')
def hotel_manager_dashboard(request):
    return render(request, 'users/hotel_manager_dashboard.html')


#



def loginUser(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist as e:
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
                return redirect('agencies')
            elif user_account.role == 'admin':
                return redirect('admin')
            elif user_account.role == 'hotel':
                return redirect('hotels')
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





















# @login_required(login_url='login')
# def userAccount(request):
#     profile = request.user.profile

#     roles = profile.role_set.all()
#     projects = profile.project_set.all()

#     context = {'profile': profile, 'roles': roles, 'projects': projects}
#     return render(request, 'users/account.html', context)


# @login_required(login_url='login')
# def editAccount(request):
#     profile = request.user.profile
#     profile, created = profile.objects.get_or_create(user=request.user)

#     context = {'form': fork}
#     return render(request, 'users/profile_form.html', context)
# def RegisterUser(request):
#     form = RegisterForm(request.POST)
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     context = {'form': form
#         }
        
#     return render(request, 'users/register.html', context)

                                    
# @login_required(login_url='login')
# def createRole(request):
#     profile = request.user.profile
#     form = RoleForm()

#     if request.method == 'POST':
#         form = RoleForm(request.POST)
#         if form.is_valid():
#             role = form.save(commit=False)
#             role.owner = profile
#             role.save()
#             messages.success(request, 'Role was added successfully!')
#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'users/role_form.html', context)


# @login_required(login_url='login')
# def updateRole(request, pk):
#     profile = request.user.profile
#     role = profile.role_set.get(id=pk)
#     form = RoleForm(instance=role)

#     if request.method == 'POST':
#         form = RoleForm(request.POST, instance=role)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Role was updated successfully!')
#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'users/role_form.html', context)


# @login_required(login_url='login')
# def deleteRole(request, pk):
#     profile = request.user.profile
#     role = profile.role_set.get(id=pk)
#     if request.method == 'POST':
#         role.delete()
#         messages.success(request, 'Role was deleted successfully!')
#         return redirect('account')

#     context = {'object': role}
#     return render(request, 'delete_template.html', context)


# @login_required(login_url='login')
# def inbox(request):
#     profile = request.user.profile
#     messageRequests = profile.messages.all()
#     unreadCount = messageRequests.filter(is_read=False).count()
#     context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
#     return render(request, 'users/inbox.html', context)


# @login_required(login_url='login')
# def viewMessage(request, pk):
#     profile = request.user.profile
#     message = profile.messages.get(id=pk)
#     if message.is_read == False:
#         message.is_read = True
#         message.save()
#     context = {'message': message}
#     return render(request, 'users/message.html', context)


# def createMessage(request, pk):
#     recipient = Profile.objects.get(id=pk)
#     form = MessageForm()

#     try:
#         sender = request.user.profile
#     except:
#         sender = None

#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = sender
#             message.recipient = recipient

#             if sender:
#                 message.name = sender.name
#                 message.email = sender.email
#             message.save()

#             messages.success(request, 'Your message was successfully sent!')
#             return redirect('user-profile', pk=recipient.id)

#     context = {'recipient': recipient, 'form': form}
#     return render(request, 'users/message_form.html', context)

#create function for managing user profile
# def create_user_profile(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
            
#     #check if user is already logged in
#     if request.user.is_authenticated:
#         return redirect('account')