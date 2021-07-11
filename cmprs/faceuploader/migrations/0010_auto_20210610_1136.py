# Generated by Django 3.1.6 on 2021-06-10 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceuploader', '0009_remove_face_image_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face_image',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='face_image',
            name='missing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 11, 36, 46, 560370)),
        ),
    ]
