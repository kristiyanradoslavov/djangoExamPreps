# album urls

from django.urls import path, include
from musicAppProject.album.views import album_add, album_details, album_edit, album_delete

urlpatterns = [
    path('add/', album_add, name='album add'),
    path('details/<id>/', album_details, name='album details'),
    path('edit/<id>/', album_edit, name='album edit'),
    path('delete/<id>/', album_delete, name='album delete'),
]
