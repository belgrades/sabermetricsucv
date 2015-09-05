# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SabermetricsUCV', '0006_auto_20150902_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batting',
            name='id',
            field=models.IntegerField(serialize=False, db_column='id', primary_key=True),
        ),
        migrations.AlterField(
            model_name='fielding',
            name='id',
            field=models.IntegerField(serialize=False, db_column='id', primary_key=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='id',
            field=models.IntegerField(serialize=False, db_column='id', primary_key=True),
        ),
    ]
