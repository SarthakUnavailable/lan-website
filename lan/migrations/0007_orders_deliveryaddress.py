# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0006_auto_20141228_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='deliveryaddress',
            field=models.CharField(default=b'0', max_length=50),
            preserve_default=True,
        ),
    ]
