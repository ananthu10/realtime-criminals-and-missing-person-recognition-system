from django import forms
from .models import Face_image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Face_image
        fields = '__all__'
        labels = {'photo': 'Add front face image '}
        widgets = {
            'photo': forms.FileInput(attrs={'type': 'file'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'missing_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})

        }
