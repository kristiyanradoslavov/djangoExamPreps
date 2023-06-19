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
