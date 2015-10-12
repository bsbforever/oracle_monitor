# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0010_mssqllist_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertevent',
            name='issuedate',
            field=models.CharField(default='2014/12/08', max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
