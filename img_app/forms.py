from django import forms
from django.core.exceptions import ValidationError
from .models import ImageModel, ImageUpdate


class ImageFormAdd(forms.ModelForm):
    """ Форма добавления изображений """

    def clean(self):
        super().clean()
        image_url = self.cleaned_data['image_url']
        image_loc = self.cleaned_data['image_loc']
        if image_loc and image_url:
            errors = {'image_url': ValidationError(
                'Заполните только одно поле', code='wrong_1')}
            raise ValidationError(errors)
        if image_url.strip() == '' and image_loc == None:
            raise ValidationError('Введите данные в одно из полей')

    class Meta:
        model = ImageModel
        fields = ('image_url', 'image_loc')


class ImageUpdateForm(forms.ModelForm):
    """ Форма изменения размеров изображений """

    class Meta:
        model = ImageUpdate
        fields = ('width', 'height')

    def clean_height(self):
        """пользовательская валидация"""
        #height = self.cleaned_data['height']
        #if len(height) > 5
            #raise ValidationError('Слишком большой размер')
        #return heigth
        pass
