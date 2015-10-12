# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0012_auto_20141215_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertevent',
            name='eventdate',
        ),
        migrations.AddField(
            model_name='alertevent',
            name='control',
            field=models.CharField(default='OK', max_length=10, blank=True),
            preserve_default=False,
        ),
    ]
