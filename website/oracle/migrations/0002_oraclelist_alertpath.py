# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oraclelist',
            name='alertpath',
            field=models.CharField(default='alert', max_length=300),
            preserve_default=False,
        ),
    ]
