# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SabermetricsUCV', '0009_auto_20150902_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitching',
            name='lob',
            field=models.DecimalField(max_digits=65, db_column='LOB', decimal_places=30),
        ),
    ]
