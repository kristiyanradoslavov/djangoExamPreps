from django import forms

from MyPlantApp.common_and_plants.models import Plant
from MyPlantApp.users.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class CreateProfileForm(ProfileBaseForm):
    pass


class EditProfileForm(ProfileBaseForm):
    pass


class DeleteProfileForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hide_fields()

    def save(self, commit=True):
        if commit:
            Plant.objects. \
                all(). \
                delete()
            self.instance.delete()

        return self.instance

    def __hide_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()
