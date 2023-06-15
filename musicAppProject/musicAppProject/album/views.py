# album views

from django.shortcuts import render, redirect

from musicAppProject.album.forms import CreateAlbumForm
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
        'account': get_account(),
        'form': form
    }

    return render(request, 'album/add-album.html', context)


def album_details(request, id):
    return render(request, 'album/album-details.html')


def album_edit(request, id):
    return render(request, 'album/edit-album.html')


def album_delete(request, id):
    return render(request, 'album/delete-album.html')
