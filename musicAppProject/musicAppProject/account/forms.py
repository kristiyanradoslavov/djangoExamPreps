from django import forms

from musicAppProject.account.models import Profile


class RegistrationForm(forms.ModelForm):
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
