# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0002_auto_20141205_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderid', models.CharField(default=b'0', max_length=10)),
                ('meters_quantity', models.CharField(default=b'0', max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('feedback', models.CharField(default=b'0', max_length=100)),
                ('cust_ph', models.ForeignKey(to='lan.info')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='info',
            name='name',
        ),
        migrations.AddField(
            model_name='info',
            name='GenderIsMale',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='info',
            name='TotalOrders',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='info',
            name='address',
            field=models.CharField(default=b'1', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.CharField(default=b'1', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='info',
            name='fname',
            field=models.CharField(default=b'1', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='info',
            name='lname',
            field=models.CharField(default=b'1', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='info',
            name='verify',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
