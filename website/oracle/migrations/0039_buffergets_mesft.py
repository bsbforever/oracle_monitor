# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0038_sortusagetext'),
    ]

    operations = [
        migrations.CreateModel(
            name='buffergets_mesft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('buffer_gets_count', models.BigIntegerField(blank=True)),
                ('executions', models.BigIntegerField(blank=True)),
                ('cpu_time', models.BigIntegerField(blank=True)),
                ('elapsed_time', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
