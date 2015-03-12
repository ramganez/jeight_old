# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0015_auto_20150312_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 23, 38, 41, 713881)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 23, 38, 41, 710431)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='mail_id',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='mobile',
            field=models.CharField(max_length=12, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 23, 38, 41, 718079), blank=True),
            preserve_default=True,
        ),
    ]
