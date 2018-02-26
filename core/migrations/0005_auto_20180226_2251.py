# Generated by Django 2.0 on 2018-02-26 20:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180226_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='gamestate',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 26, 20, 51, 19, 470159, tzinfo=utc)),
        ),
    ]
