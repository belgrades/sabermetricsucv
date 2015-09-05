# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SabermetricsUCV', '0008_auto_20150902_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batting',
            name='avg',
            field=models.DecimalField(decimal_places=30, db_column='AVG', max_digits=65),
        ),
        migrations.AlterField(
            model_name='batting',
            name='babip',
            field=models.DecimalField(decimal_places=30, db_column='BABIP', max_digits=65),
        ),
        migrations.AlterField(
            model_name='batting',
            name='iso',
            field=models.DecimalField(decimal_places=30, db_column='ISO', max_digits=65),
        ),
        migrations.AlterField(
            model_name='batting',
            name='obp',
            field=models.DecimalField(decimal_places=30, db_column='OBP', max_digits=65),
        ),
        migrations.AlterField(
            model_name='batting',
            name='ops',
            field=models.DecimalField(decimal_places=30, db_column='OPS', max_digits=65),
        ),
        migrations.AlterField(
            model_name='batting',
            name='slg',
            field=models.DecimalField(decimal_places=30, db_column='SLG', max_digits=65),
        ),
        migrations.AlterField(
            model_name='batting',
            name='woba',
            field=models.DecimalField(decimal_places=30, db_column='wOBA', max_digits=65),
        ),
        migrations.AlterField(
            model_name='fielding',
            name='fp',
            field=models.DecimalField(decimal_places=30, db_column='FP', max_digits=65),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='avg',
            field=models.DecimalField(decimal_places=30, db_column='AVG', max_digits=65),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='babip',
            field=models.DecimalField(decimal_places=30, db_column='BABIP', max_digits=65),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='lob',
            field=models.DecimalField(decimal_places=30, db_column='LOB%', max_digits=65),
        ),
    ]
