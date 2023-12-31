# album urls

from django.urls import path, include
from musicAppProject.album.views import album_add, album_details, album_edit, album_delete

urlpatterns = [
    path('add/', album_add, name='album add'),
    path('details/<int:pk>/', album_details, name='album details'),
    path('edit/<int:pk>/', album_edit, name='album edit'),
    path('delete/<int:pk>/', album_delete, name='album delete'),
]
