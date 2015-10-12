# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0021_oraclelist_monitor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='oraclestatus',
            name='archiver',
            field=models.CharField(default=b'opened', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oraclestatus',
            name='host_name',
            field=models.CharField(default=b'host', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oraclestatus',
            name='startup_time',
            field=models.CharField(default=b'2015', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oraclestatus',
            name='status',
            field=models.CharField(default=b'opened', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oraclestatus',
            name='version',
            field=models.CharField(default=b'10', max_length=50),
            preserve_default=True,
        ),
    ]
