# Generated by Django 2.0.2 on 2018-02-26 18:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180226_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestate',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 26, 18, 35, 39, 321238, tzinfo=utc)),
        ),
    ]