# account views

from django.shortcuts import render, redirect

from musicAppProject.account.forms import ProfileDeleteForm
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

    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(
        request,
        'account/profile-delete.html',
        context
    )
