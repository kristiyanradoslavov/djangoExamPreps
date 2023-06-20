from django import forms

from MyPlantApp.common_and_plants.models import Plant


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

        labels = {
            'plant_type': 'Type',
            'name': 'Name',
            'image_url': 'Image URL',
            'description': "Description",
            'price': 'Price',
        }


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(BasePlantForm):
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
