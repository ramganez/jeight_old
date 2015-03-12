# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0008_auto_20150311_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareexpenses',
            name='month',
            field=models.CharField(default=b'March', max_length=10),
            preserve_default=True,
        ),
    ]
