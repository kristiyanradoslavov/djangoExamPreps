from django import forms

from CarCollection.car.models import Car


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        labels = {
            'image_url': 'Image URL'
        }


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.required = False
