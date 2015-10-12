# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0016_alertevent_createdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertevent',
            name='createdate',
        ),
    ]
