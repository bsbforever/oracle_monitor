# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0009_mssqllist'),
    ]

    operations = [
        migrations.AddField(
            model_name='mssqllist',
            name='content',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
    ]
