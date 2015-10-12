# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0050_linuxlist_performance_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='topevent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('wait_time', models.BigIntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
