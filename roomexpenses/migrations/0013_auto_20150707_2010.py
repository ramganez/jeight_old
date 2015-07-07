# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0012_auto_20150707_2010'),
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
    ]
