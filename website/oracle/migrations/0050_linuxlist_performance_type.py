# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0049_auto_20150803_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='linuxlist',
            name='performance_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
