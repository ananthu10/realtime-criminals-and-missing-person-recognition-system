from django.contrib import admin

# Register your models here.
from .models import image


@admin.register(image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'name', 'date']
