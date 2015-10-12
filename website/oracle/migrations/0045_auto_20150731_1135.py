# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0044_auto_20150730_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oracle_buffergets',
            name='sql_time',
            field=models.BigIntegerField(blank=True),
            preserve_default=True,
        ),
    ]
