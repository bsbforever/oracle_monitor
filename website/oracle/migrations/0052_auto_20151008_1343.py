# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0051_topevent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='topevent',
            new_name='oracle_topevent',
        ),
    ]
