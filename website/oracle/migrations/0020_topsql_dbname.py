# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0019_topsql'),
    ]

    operations = [
        migrations.AddField(
            model_name='topsql',
            name='dbname',
            field=models.CharField(default='s', max_length=50),
            preserve_default=False,
        ),
    ]
