# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('mail_id', models.CharField(max_length=12)),
                ('check_in', models.DateField(default=datetime.date.today)),
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
                ('mail_id', models.CharField(max_length=12)),
                ('advance_given', models.DecimalField(max_digits=4, decimal_places=2)),
                ('other_exp_paid', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
