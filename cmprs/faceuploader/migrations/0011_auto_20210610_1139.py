# Generated by Django 3.1.6 on 2021-06-10 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceuploader', '0010_auto_20210610_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face_image',
            name='missing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 11, 39, 2, 781186)),
        ),
    ]
