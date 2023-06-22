from django import forms

from gamesPlayApp.games.models import Game


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

        labels = {
            'max_level': "Max Level",
            'image_url': 'Image URL',
        }


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
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
