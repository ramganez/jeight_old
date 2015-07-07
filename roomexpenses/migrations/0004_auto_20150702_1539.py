# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0003_auto_20150702_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 15, 39, 26, 373982)),
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 7, 2, 15, 39, 26, 373410)),
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 15, 39, 26, 374575), blank=True),
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='is_duplicate',
            field=models.BooleanField(default=False),
        ),
    ]
