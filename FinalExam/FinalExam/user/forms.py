from django import forms

from FinalExam.user.models import Profile
from FinalExam.util_functions.get_fruits import get_all_fruits


class CreateProfileForm(forms.ModelForm):
    class Meta:
        FIRST_NAME_PLACEHOLDER = 'First Name'
        LAST_NAME_PLACEHOLDER = 'Last Name'
        EMAIL_PLACEHOLDER = 'Email'
        PASSWORD_PLACEHOLDER = 'Password'

        model = Profile
        exclude = ('image_url', 'age')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': FIRST_NAME_PLACEHOLDER
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': LAST_NAME_PLACEHOLDER
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': EMAIL_PLACEHOLDER
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': PASSWORD_PLACEHOLDER,
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('email', 'password',)

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hide_fields()

    def save(self, commit=True):
        fruits = get_all_fruits()

        if commit:
            fruits.delete()
            self.instance.delete()

        return self.instance

    def __hide_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()
            field.required = False
