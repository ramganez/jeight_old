# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0002_auto_20141113_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommember',
            name='advance_given',
            field=models.DecimalField(max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roommember',
            name='other_exp_paid',
            field=models.DecimalField(max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
