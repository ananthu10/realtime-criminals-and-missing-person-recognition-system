# Generated by Django 3.1.6 on 2021-02-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recognize',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
