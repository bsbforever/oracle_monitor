# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0035_oraclelist_performance_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='topsql_diskread',
            new_name='topsql_diskreads',
        ),
        migrations.RenameField(
            model_name='topsql_diskreads',
            old_name='disk_read',
            new_name='disk_reads',
        ),
    ]
