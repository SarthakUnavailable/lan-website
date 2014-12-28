# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0004_auto_20141228_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='id',
        ),
        migrations.AlterField(
            model_name='orders',
            name='DatePlaced',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderid',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
