# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0002_auto_20150630_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='shareexpenses',
            name='is_duplicate',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 14, 44, 39, 898358)),
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='month',
            field=models.CharField(default=b'July', max_length=10),
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 7, 2, 14, 44, 39, 897749)),
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 14, 44, 39, 898965), blank=True),
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='month',
            field=models.CharField(default=b'July', max_length=10),
        ),
    ]
