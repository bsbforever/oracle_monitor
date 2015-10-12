# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0034_auto_20150713_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='oraclelist',
            name='performance_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
