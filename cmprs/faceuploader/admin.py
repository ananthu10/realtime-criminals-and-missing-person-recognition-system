from django.contrib import admin

# Register your models here.
from .models import Face_image
admin.site.register(Face_image)

# @admin.register(Face_image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['id', 'photo', 'name', 'date',]
