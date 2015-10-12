# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0019_auto_20141216_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertevent',
            name='createdate',
        ),
    ]
