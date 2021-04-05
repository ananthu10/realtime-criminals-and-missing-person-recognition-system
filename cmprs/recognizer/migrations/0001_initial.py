# Generated by Django 3.1.6 on 2021-04-05 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faceuploader', '0008_auto_20210405_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recognize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='myphoto/%Y/%m/%d/')),
                ('location', models.CharField(default='no-locaton', max_length=100)),
                ('latitude', models.FloatField(default=0.0, max_length=20)),
                ('longitude', models.FloatField(default=0.0, max_length=20)),
                ('image_taken_time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('face_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faceuploader.face_image')),
            ],
        ),
    ]
