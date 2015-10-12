# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0011_alertevent_issuedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='oraclelist',
            name='charset',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oraclelist',
            name='ncharset',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
    ]
