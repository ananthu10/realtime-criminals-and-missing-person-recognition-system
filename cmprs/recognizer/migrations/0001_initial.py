# Generated by Django 3.1.6 on 2021-04-05 10:43

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
                ('location', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('latitude', models.CharField(default='DEFAULT VALUE', max_length=20)),
                ('longitude', models.CharField(default='DEFAULT VALUE', max_length=20)),
                ('current_time', models.CharField(default='no time bruh!', max_length=20)),
                ('face_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faceuploader.face_image')),
            ],
        ),
    ]
