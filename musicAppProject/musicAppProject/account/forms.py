from django import forms

from musicAppProject.account.models import Profile
from musicAppProject.album.models import Album


class BaseForm(forms.ModelForm):
    class Meta:
        USERNAME_PLACEHOLDER = 'Username'
        EMAIL_PLACEHOLDER = 'Email'
        AGE_PLACEHOLDER = 'Age'

        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': USERNAME_PLACEHOLDER}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': EMAIL_PLACEHOLDER}
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': AGE_PLACEHOLDER}
            ),
        }


class RegistrationForm(BaseForm):
    pass


class ProfileDeleteForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hide_inputs()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __hide_inputs(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
