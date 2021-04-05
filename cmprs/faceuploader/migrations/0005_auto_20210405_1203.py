# Generated by Django 3.1.6 on 2021-04-05 06:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faceuploader', '0004_auto_20210405_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face_image',
            name='incidentlocation',
        ),
        migrations.RemoveField(
            model_name='face_image',
            name='missingdate',
        ),
        migrations.AddField(
            model_name='face_image',
            name='inciden_tlocation',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='face_image',
            name='missing_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='face_image',
            name='description',
            field=models.CharField(default='no data', max_length=200),
        ),
    ]
