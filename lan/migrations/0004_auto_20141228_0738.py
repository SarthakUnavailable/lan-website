# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0003_auto_20141214_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='cust_ph',
            new_name='custph',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='meters_quantity',
            new_name='metersquantity',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='feedback',
        ),
        migrations.AddField(
            model_name='orders',
            name='DatePlaced',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 7, 38, 16, 564406, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
    ]
