# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0043_auto_20150730_1723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='buffergets',
            new_name='oracle_buffergets',
        ),
    ]
