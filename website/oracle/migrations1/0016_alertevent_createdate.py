# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0015_remove_alertevent_createdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertevent',
            name='createdate',
            field=models.DateField(default=datetime.datetime(2014, 12, 16, 3, 49, 16, 419328, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
