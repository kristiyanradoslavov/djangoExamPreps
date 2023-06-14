# album views

from django.shortcuts import render


def album_add(request):
    return render(request, 'album/add-album.html')


def album_details(request, id):
    return render(request, 'album/album-details.html')


def album_edit(request, id):
    return render(request, 'album/edit-album.html')


def album_delete(request, id):
    return render(request, 'album/delete-album.html')
