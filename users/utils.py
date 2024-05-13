from users.models import UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = UserProfile.objects.filter(name__icontains=search_query)
    return profiles, search_query
def paginateProfiles(request, profile):
    paginator = Paginator(profiles, 3)
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)
    return profiles