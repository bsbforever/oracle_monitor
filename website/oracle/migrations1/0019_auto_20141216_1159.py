# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0018_alertevent_createdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertevent',
            name='createdate',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
