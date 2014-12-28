# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0005_auto_20141228_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='orderid',
        ),
        migrations.AddField(
            model_name='orders',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
