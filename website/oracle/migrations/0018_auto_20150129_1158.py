# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0017_linuxlist_hostname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linuxlist',
            name='id',
        ),
        migrations.AlterField(
            model_name='linuxlist',
            name='ipaddress',
            field=models.GenericIPAddressField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
