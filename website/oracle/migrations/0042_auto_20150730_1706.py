# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0041_auto_20150730_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buffergets_mesft',
            name='elapsed_time',
            field=models.BigIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
