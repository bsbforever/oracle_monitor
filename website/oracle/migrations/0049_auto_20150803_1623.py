# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0048_oracle_cputime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oracle_cputime',
            name='disk_reads',
        ),
        migrations.RemoveField(
            model_name='oracle_elapsedtime',
            name='disk_reads',
        ),
    ]
