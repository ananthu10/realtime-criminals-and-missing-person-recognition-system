import django_filters

from .models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Face_image
        fields = ['name', 'case', 'missing_date']
      #   widgets = {
      #       'missing_date': forms.DateInput(attrs={'type': 'date'}),
      #   }
      #   #exclude = ['photo']
