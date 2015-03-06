# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0003_auto_20141113_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyExpense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(default=b'November', max_length=10)),
                ('rent', models.DecimalField(max_digits=7, decimal_places=2)),
                ('cable', models.DecimalField(max_digits=5, decimal_places=2)),
                ('electricity', models.DecimalField(max_digits=5, decimal_places=2)),
                ('last_month_exp', models.DecimalField(max_digits=7, decimal_places=2)),
                ('next_month_exp', models.DecimalField(max_digits=7, decimal_places=2)),
                ('grand_total', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
