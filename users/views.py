from os import fork
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import searchProfiles, paginateProfiles
from .forms import UserRegistrationForm
from .forms import UserLoginForm


def loginUser(request):
    page: 'login'
    form = UserLoginForm()
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', 'account'))
            else:
                messages.error(request, 'Username OR password is incorrect')
    
    else:
        form = UserLoginForm()
        
    return render(request, 'users/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/register.html', context)


def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {'profiles': profiles, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = profile.objects.get(id=pk)

    topRoles = profile.role_set.exclude(description__exact="")
    otherRoles = profile.role_set.filter(description="")

    context = {'profile': profile, 'topRoles': topRoles,
               "otherRoles": otherRoles}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    roles = profile.role_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'roles': roles, 'projects': projects}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    profile, created = profile.objects.get_or_create(user=request.user)

    context = {'form': fork}
    return render(request, 'users/profile_form.html', context)

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
def create_user_profile(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
    #check if user is already logged in
    if request.user.is_authenticated:
        return redirect('account')