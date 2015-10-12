# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0031_topsql_buffergets_topsql_cputime_topsql_diskread_topsql_elapsedtime_topsql_sharablememo_topsql_sorts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='topsql_sharablememo',
            new_name='topsql_sharablemem',
        ),
    ]
