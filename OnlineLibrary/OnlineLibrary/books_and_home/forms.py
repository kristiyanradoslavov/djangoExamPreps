from django import forms

from OnlineLibrary.books_and_home.models import Book


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                    'id': 'title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'cols': '40',
                    'rows': '100',
                    'id': 'description'
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                    'id': 'image'
                }
            ),

            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                    'id': 'type'
                }
            ),

        }


class AddBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass
