# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0016_linuxlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='linuxlist',
            name='hostname',
            field=models.CharField(default='linux', max_length=100),
            preserve_default=False,
        ),
    ]
