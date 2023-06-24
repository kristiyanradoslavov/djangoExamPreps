from django import forms

from FinalExam.fruits.models import Fruit


class CreateFruitForm(forms.ModelForm):
    class Meta:
        NAME_PLACEHOLDER = 'Fruit Name'
        IMAGE_PLACEHOLDER = 'Fruit Image URL'
        DESCRIPTION_PLACEHOLDER = 'Fruit Description'
        NUTRITION_PLACEHOLDER = 'Nutrition Info'

        model = Fruit
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': NAME_PLACEHOLDER,
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': IMAGE_PLACEHOLDER,
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': DESCRIPTION_PLACEHOLDER,
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': NUTRITION_PLACEHOLDER,
                }
            ),
        }
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': "Name",
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('nutrition',)

        labels = {
            'name': "Name",
            'image_url': 'Image URL',
            'description': 'Description',
        }

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
