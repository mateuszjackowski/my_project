# Generated by Django 3.1.1 on 2020-09-13 12:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_auto_20200913_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='executor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sample',
            name='date_of_production',
            field=models.DateField(default=datetime.datetime(2020, 9, 13, 12, 24, 5, 293895)),
        ),
    ]