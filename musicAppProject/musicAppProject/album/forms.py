from django import forms

from musicAppProject.album.models import Album
from musicAppProject.album.utils import get_all_available_genres


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        ALBUM_NAME_PLACEHOLDER = "Album Name"
        ARTIST_PLACEHOLDER = "Artist"
        DESCRIPTION_PLACEHOLDER = "Description"
        URL_PLACEHOLDER = "Image URL"
        PRICE_PLACEHOLDER = "Price"
        GENRE_CHOICES = get_all_available_genres()
        model = Album

        fields = '__all__'
        # widgets = {
        #     "album_name": forms.Textarea(
        #         attrs={'placeholder': ALBUM_NAME_PLACEHOLDER}
        #     ),
        #     "artist": forms.Textarea(
        #         attrs={'placeholder': ARTIST_PLACEHOLDER}
        #     )
        # }
