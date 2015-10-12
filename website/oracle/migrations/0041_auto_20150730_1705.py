# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0040_auto_20150730_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buffergets_mesft',
            name='cpu_time',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='buffergets_mesft',
            name='module',
            field=models.CharField(max_length=65, null=True),
            preserve_default=True,
        ),
    ]
