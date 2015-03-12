# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0007_auto_20150305_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareExpenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_to_be_given', models.DecimalField(max_digits=6, decimal_places=2)),
                ('month', models.ForeignKey(to='roomexpenses.MonthlyExpense')),
                ('other_member', models.ForeignKey(to='roomexpenses.OtherMember')),
                ('room_member', models.ForeignKey(to='roomexpenses.RoomMember')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='othermember',
            name='in_room',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='roommember',
            name='in_room',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
