from django import forms
from .models import Video_File


class Video_File_Form(forms.ModelForm):
    class Meta:
        model = Video_File
        fields = '__all__'
