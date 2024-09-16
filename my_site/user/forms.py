from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = "Группа не выбрана"

    class Meta:
        model = User
        fields = ['name', 'patronymic', 'surname', 'slug', 'autobiography', 'photo', 'group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'autobiography': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return name
