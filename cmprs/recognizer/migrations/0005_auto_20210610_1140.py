# Generated by Django 3.1.6 on 2021-06-10 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognizer', '0004_auto_20210610_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recognize',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 10, 11, 40, 26, 630213)),
        ),
    ]
