from django import forms
from .models import Face_image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Face_image
        fields = '__all__'
        labels = {'photo': ' '}
