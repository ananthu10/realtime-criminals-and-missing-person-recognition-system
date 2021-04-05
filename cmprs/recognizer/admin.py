from django.contrib import admin

# Register your models here.
from .models import Recognize


# @admin.register(Recognize)
# class RecoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'face_id', 'image', 'location',
#                     'latitude', 'longitude', 'image_taken_time']
admin.site.register(Recognize)
