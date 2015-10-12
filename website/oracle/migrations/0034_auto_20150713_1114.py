# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0033_auto_20150713_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topsql_buffergets',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql_cputime',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql_diskread',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql_elapsedtime',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql_sharablemem',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql_sorts',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql_version',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
    ]
