# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0026_mssqllist_monitor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='mssqllist',
            name='hostname',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
