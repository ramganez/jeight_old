# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='othermember',
            name='in_room',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 30, 20, 26, 23, 203944)),
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 6, 30, 20, 26, 23, 203385)),
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 30, 20, 26, 23, 204555), blank=True),
        ),
    ]
