# Generated by Django 3.1.6 on 2021-04-03 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceuploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='face_image',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
