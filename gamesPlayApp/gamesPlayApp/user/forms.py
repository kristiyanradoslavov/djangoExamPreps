from django import forms

from gamesPlayApp.user.models import Profile
from gamesPlayApp.util_functions.get_games import get_all_games


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hide_fields()

    def save(self, commit=True):
        games = get_all_games()
        if commit:
            games.delete()
            self.instance.delete()

        return self.instance

    def __hide_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()
