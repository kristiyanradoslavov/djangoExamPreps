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

        widgets = {
            "album_name": forms.TextInput(
                attrs={'placeholder': ALBUM_NAME_PLACEHOLDER}
            ),
            "artist": forms.TextInput(
                attrs={'placeholder': ARTIST_PLACEHOLDER}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': DESCRIPTION_PLACEHOLDER}
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': URL_PLACEHOLDER}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': PRICE_PLACEHOLDER}
            )
        }

    # def clean_price(self):
    #     price = self.cleaned_data['price']
    #
    #     return f"{price:.0f}"
