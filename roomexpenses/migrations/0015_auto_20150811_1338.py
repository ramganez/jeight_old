# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0014_auto_20150807_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='othermember',
            old_name='x_field',
            new_name='some_amount',
        ),
        migrations.AlterField(
            model_name='othermember',
            name='ready_to_share',
            field=models.CharField(default=b'all', max_length=4, choices=[(b'all', b'All'), (b'some_amount', b'I can pay'), (b'rent', b'Rent+Maintenance'), (b'food', b'Food Only'), (b'none', b'None')]),
        ),
    ]
