from django import forms

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
