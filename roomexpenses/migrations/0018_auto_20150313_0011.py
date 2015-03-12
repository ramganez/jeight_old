# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0017_auto_20150313_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 0, 11, 48, 794539)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 0, 11, 48, 791234)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='mail_id',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 0, 11, 48, 798664), blank=True),
            preserve_default=True,
        ),
    ]
