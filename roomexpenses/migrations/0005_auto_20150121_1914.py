# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0004_monthlyexpense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyexpense',
            name='month',
            field=models.CharField(default=b'January', max_length=10),
            preserve_default=True,
        ),
    ]
