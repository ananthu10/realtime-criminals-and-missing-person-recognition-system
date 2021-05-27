# Generated by Django 3.1.6 on 2021-05-27 17:27

from django.db import migrations, models
import videoreco.models


class Migration(migrations.Migration):

    dependencies = [
        ('videoreco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_file',
            name='case_details',
            field=models.TextField(default='No case data givem', max_length=60),
        ),
        migrations.AddField(
            model_name='video_file',
            name='end_time',
            field=models.DateTimeField(default=videoreco.models.default_start_time),
        ),
        migrations.AddField(
            model_name='video_file',
            name='start_time',
            field=models.DateTimeField(default=videoreco.models.default_start_time),
        ),
        migrations.AddField(
            model_name='video_file',
            name='v_location',
            field=models.CharField(default='No location given', max_length=30),
        ),
    ]
