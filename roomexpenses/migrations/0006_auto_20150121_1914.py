# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0005_auto_20150121_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='grand_total',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
