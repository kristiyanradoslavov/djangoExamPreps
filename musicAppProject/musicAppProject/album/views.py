# album views

from django.shortcuts import render, redirect

from musicAppProject.album.forms import CreateAlbumForm
from musicAppProject.album.models import Album
from musicAppProject.common.utils import get_account
from musicAppProject.common.views import index


def album_add(request):
    if request.method == "GET":
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)

    context = {
        'profile': get_account(),
        'form': form
    }

    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def album_edit(request, pk):
    return render(request, 'album/edit-album.html')


def album_delete(request, pk):
    return render(request, 'album/delete-album.html')
