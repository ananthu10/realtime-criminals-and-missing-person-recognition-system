# Generated by Django 3.1.6 on 2021-04-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceuploader', '0006_auto_20210405_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face_image',
            name='description',
            field=models.TextField(default='no data', max_length=200),
        ),
    ]
