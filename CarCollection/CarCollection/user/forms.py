from django import forms

from CarCollection.user.models import Profile
from CarCollection.util_functions.get_cars import get_cars


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')

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
        all_cars = get_cars()
        if commit:
            all_cars.delete()
            self.instance.delete()

        return self.instance

    def __hide_fields(self):
        for field in self.fields.values():
            field.widget = forms.HiddenInput()
