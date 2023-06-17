# account views

from django.shortcuts import render

from musicAppProject.album.models import Album
from musicAppProject.common.utils import get_account


def profile_details(request):
    album_count = Album.objects.count()

    context = {
        'profile': get_account(),
        'album_count': album_count
    }
    return render(request, 'account/profile-details.html', context)


def profile_delete(request):
    profile = get_account()
    # profile.delete()

    context = {
        'profile': profile
    }

    return render(request, 'account/profile-delete.html', context)
