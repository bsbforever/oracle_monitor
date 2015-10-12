# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0007_oraclestatus_ipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertevent',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
