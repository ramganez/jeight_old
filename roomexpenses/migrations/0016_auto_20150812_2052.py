# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0015_auto_20150811_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='othermember',
            name='ready_to_share',
            field=models.CharField(default=b'all', max_length=11, choices=[(b'all', b'All'), (b'some_amount', b'I can pay'), (b'rent', b'Rent+Maintenance'), (b'food', b'Food Only'), (b'none', b'None')]),
        ),
    ]
