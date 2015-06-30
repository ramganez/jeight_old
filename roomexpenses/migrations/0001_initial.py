# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyExpense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(default=b'June', max_length=10)),
                ('rent', models.DecimalField(default=7500, max_digits=7, decimal_places=2)),
                ('cable', models.DecimalField(default=100, max_digits=7, decimal_places=2)),
                ('electricity', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('maintenance', models.DecimalField(default=350, max_digits=7, decimal_places=2)),
                ('water', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('last_month_exp', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('next_month_exp', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('grand_total', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2015, 6, 30, 20, 25, 7, 19172))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12, null=True, blank=True)),
                ('mail_id', models.EmailField(max_length=75, null=True, blank=True)),
                ('check_in', models.DateField(default=datetime.datetime(2015, 6, 30, 20, 25, 7, 18623))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('mail_id', models.EmailField(max_length=75)),
                ('advance_given', models.DecimalField(max_digits=6, decimal_places=2)),
                ('other_exp_paid', models.DecimalField(max_digits=6, decimal_places=2)),
                ('in_room', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShareExpenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(default=b'June', max_length=10)),
                ('room_member_share', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('other_member_share', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2015, 6, 30, 20, 25, 7, 19785), blank=True)),
                ('other_member', models.ForeignKey(to='roomexpenses.OtherMember', null=True)),
                ('room_member', models.ForeignKey(to='roomexpenses.RoomMember', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
