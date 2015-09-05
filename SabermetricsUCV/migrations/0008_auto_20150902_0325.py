# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SabermetricsUCV', '0007_auto_20150902_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batting',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='fielding',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
