# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomexpenses', '0009_auto_20150311_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareexpenses',
            name='other_member',
            field=models.ForeignKey(to='roomexpenses.OtherMember', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareexpenses',
            name='room_member',
            field=models.ForeignKey(to='roomexpenses.RoomMember', null=True),
            preserve_default=True,
        ),
    ]
