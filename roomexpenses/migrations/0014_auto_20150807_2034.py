# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0013_auto_20150707_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='othermember',
            name='ready_to_share',
            field=models.CharField(default=b'all', max_length=4, choices=[(b'all', b'All'), (b'xxx', b'XXX'), (b'rent', b'Rent+Maintenance'), (b'food', b'Food Only'), (b'none', b'None')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='othermember',
            name='x_field',
            field=models.DecimalField(default=2000, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='month',
            field=models.CharField(default=b'August', max_length=10),
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='month',
            field=models.CharField(default=b'August', max_length=10),
        ),
    ]
