# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SabermetricsUCV', '0002_auto_20150901_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('cedula', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='batting',
            options={},
        ),
        migrations.AlterModelOptions(
            name='fielding',
            options={},
        ),
        migrations.AlterModelOptions(
            name='pitching',
            options={},
        ),
        migrations.AlterModelTable(
            name='batting',
            table=None,
        ),
        migrations.AlterModelTable(
            name='fielding',
            table=None,
        ),
        migrations.AlterModelTable(
            name='pitching',
            table=None,
        ),
    ]
