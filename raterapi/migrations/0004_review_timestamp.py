# Generated by Django 3.1.3 on 2020-11-06 21:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('raterapi', '0003_auto_20201106_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 21, 44, 34, 896875, tzinfo=utc)),
        ),
    ]