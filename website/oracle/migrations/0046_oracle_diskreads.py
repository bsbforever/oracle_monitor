# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0045_auto_20150731_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='oracle_diskreads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.BigIntegerField(blank=True)),
                ('sql_id', models.CharField(max_length=50)),
                ('disk_reads', models.BigIntegerField(blank=True)),
                ('executions', models.BigIntegerField(blank=True)),
                ('cpu_time', models.BigIntegerField(null=True, blank=True)),
                ('elapsed_time', models.BigIntegerField(null=True, blank=True)),
                ('module', models.CharField(max_length=65, null=True)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
