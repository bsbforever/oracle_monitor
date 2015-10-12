# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0013_auto_20141216_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertevent',
            name='createdate',
            field=models.DateField(default=datetime.datetime(2014, 12, 17, 2, 34, 26, 497256, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oraclestatus',
            name='invalidobject',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
