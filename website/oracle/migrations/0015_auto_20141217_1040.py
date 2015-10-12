# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0014_auto_20141217_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oraclestatus',
            old_name='invalidobject',
            new_name='invalid_object',
        ),
        migrations.AddField(
            model_name='oraclestatus',
            name='mv_compile_state',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
