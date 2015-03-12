# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0016_auto_20150312_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 0, 3, 45, 288807)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 0, 3, 45, 285594)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='mobile',
            field=models.CharField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 0, 3, 45, 292932), blank=True),
            preserve_default=True,
        ),
    ]
