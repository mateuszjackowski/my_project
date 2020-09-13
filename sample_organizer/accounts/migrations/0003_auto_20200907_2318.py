# Generated by Django 3.1.1 on 2020-09-07 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200907_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executor',
            name='phone',
            field=models.FloatField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date_of_production',
            field=models.DateField(default=datetime.datetime(2020, 9, 7, 23, 18, 7, 319082)),
        ),
    ]
