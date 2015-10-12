# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0022_auto_20150528_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='oraclestatus',
            name='sga_size',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
