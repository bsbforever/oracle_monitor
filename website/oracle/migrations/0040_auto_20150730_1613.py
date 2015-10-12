# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0039_buffergets_mesft'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buffergets_mesft',
            old_name='buffer_gets_count',
            new_name='buffer_gets',
        ),
    ]
