# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0012_auto_20150311_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 23, 39, 55, 403958), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 23, 39, 55, 400038), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 23, 39, 55, 397060), blank=True),
            preserve_default=True,
        ),
    ]
