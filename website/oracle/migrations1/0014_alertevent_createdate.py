# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0013_auto_20141216_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertevent',
            name='createdate',
            field=models.DateField(default=20141216, auto_now_add=True),
            preserve_default=False,
        ),
    ]
