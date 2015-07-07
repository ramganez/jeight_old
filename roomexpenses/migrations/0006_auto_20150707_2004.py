# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0005_auto_20150703_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyexpense',
            name='test_created',
        ),
        migrations.RemoveField(
            model_name='monthlyexpense',
            name='test_updated',
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 7, 7, 20, 4, 7, 786832)),
        ),
    ]
