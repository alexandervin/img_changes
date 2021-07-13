from django import forms
from .models import Image

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image_url', 'image_loc')

