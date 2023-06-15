from django.contrib import admin

from musicAppProject.album.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'album_name', 'artist', 'price']