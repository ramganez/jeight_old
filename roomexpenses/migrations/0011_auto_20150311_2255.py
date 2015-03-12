# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0010_auto_20150311_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 11, 22, 55, 31, 911361), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 22, 55, 31, 908232), blank=True),
            preserve_default=True,
        ),
    ]
