# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0013_auto_20150311_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyexpense',
            name='maintenance',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthlyexpense',
            name='water',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='cable',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 16, 10, 28, 94225), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='electricity',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='last_month_exp',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='next_month_exp',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='rent',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 16, 10, 28, 91020), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 16, 10, 28, 98180), blank=True),
            preserve_default=True,
        ),
    ]
