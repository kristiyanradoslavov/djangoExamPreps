from django import forms

from OnlineLibrary.books_and_home.models import Book
from OnlineLibrary.user.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        FIRST_NAME_PLACEHOLDER = 'First Name'
        LAST_NAME_PLACEHOLDER = 'Last Name'
        URL_PLACEHOLDER = "URL"
        model = Profile
        fields = "__all__"

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': FIRST_NAME_PLACEHOLDER,
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': LAST_NAME_PLACEHOLDER,
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': URL_PLACEHOLDER,
                }
            ),
        }

        labels = {
            'first_name': "First Name",
            'last_name': "Last name",
            'image_url': 'Image URL',
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        books = Book.objects.all()
        if commit:
            books.delete()
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.required = False
