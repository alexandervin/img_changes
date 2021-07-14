from django import forms
from django.core.exceptions import ValidationError

from .models import Image


class ImageFormAdd(forms.ModelForm):
    """Форма добавления изображений"""

    def clean(self):
        super().clean()
        image_url = self.cleaned_data['image_url']
        image_loc = self.cleaned_data['image_loc']
        if image_loc and image_url:
            errors = {'image_url': ValidationError(
                'Заполните только одно поле', code='wrong_1')}
            raise ValidationError(errors)
        if self.cleaned_data['image_url'].strip() and self.cleaned_data['image_loc'].strip() == '':
            raise ValidationError('Введите данные в одно из полей')

    class Meta:
        model = Image
        fields = ('image_url', 'image_loc')
