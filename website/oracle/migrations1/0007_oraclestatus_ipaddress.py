# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0006_oraclestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='oraclestatus',
            name='ipaddress',
            field=models.GenericIPAddressField(default='10.2.3.4'),
            preserve_default=False,
        ),
    ]
