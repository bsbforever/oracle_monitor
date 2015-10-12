# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0029_auto_20150710_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topsql',
            name='buffer_gets_count',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='cpu_time',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='disk_read',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='elapsed_time',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='executions',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='sharable_mem',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='sorts',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='version_count',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
    ]
