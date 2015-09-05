# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SabermetricsUCV', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batting',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='fielding',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='pitching',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='batting',
            table='batting',
        ),
        migrations.AlterModelTable(
            name='fielding',
            table='fielding',
        ),
        migrations.AlterModelTable(
            name='pitching',
            table='pitching',
        ),
    ]
