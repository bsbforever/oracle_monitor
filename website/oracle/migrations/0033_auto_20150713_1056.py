# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0032_auto_20150713_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topsql_buffergets',
            old_name='buffer_gets_count',
            new_name='buffer_gets',
        ),
    ]
