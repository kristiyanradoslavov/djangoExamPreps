from django import forms

from musicAppProject.account.models import Profile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
