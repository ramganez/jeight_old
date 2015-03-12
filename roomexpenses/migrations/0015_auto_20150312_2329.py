# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0014_auto_20150312_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shareexpenses',
            name='amount_to_be_given',
        ),
        migrations.AddField(
            model_name='shareexpenses',
            name='other_member_share',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shareexpenses',
            name='room_member_share',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='cable',
            field=models.DecimalField(default=100, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 23, 29, 42, 910175)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='electricity',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='last_month_exp',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='maintenance',
            field=models.DecimalField(default=350, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='next_month_exp',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='rent',
            field=models.DecimalField(default=7500, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthlyexpense',
            name='water',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='othermember',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 23, 29, 42, 906942), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 12, 23, 29, 42, 914247), blank=True),
            preserve_default=True,
        ),
    ]
