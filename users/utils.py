# users/utils.py

from users.models import UserProfile


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = UserProfile.objects.filter(name__icontains=search_query)
    return profiles, search_query
