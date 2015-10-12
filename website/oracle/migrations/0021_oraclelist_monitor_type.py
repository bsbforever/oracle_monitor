# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0020_topsql_dbname'),
    ]

    operations = [
        migrations.AddField(
            model_name='oraclelist',
            name='monitor_type',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
