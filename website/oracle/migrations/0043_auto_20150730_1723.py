# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0042_auto_20150730_1706'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='buffergets_mesft',
            new_name='buffergets',
        ),
    ]
