# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='passwd',
            field=models.CharField(default=b'1', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='info',
            name='rand',
            field=models.CharField(default=b'1', max_length=21),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(default=b'1', max_length=30),
            preserve_default=True,
        ),
    ]
