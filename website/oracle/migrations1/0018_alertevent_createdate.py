# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0017_remove_alertevent_createdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertevent',
            name='createdate',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
