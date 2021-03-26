from django.contrib import admin

# Register your models here.
from .models import Recognize


@admin.register(Recognize)
class RecoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'location',
                    'latitude', 'longitude', 'current_time']
