# Generated by Django 3.1.6 on 2021-04-05 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceuploader', '0005_auto_20210405_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='face_image',
            old_name='inciden_tlocation',
            new_name='incident_location',
        ),
    ]