# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0030_auto_20150710_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='topsql_buffergets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('executions', models.BigIntegerField(blank=True)),
                ('buffer_gets_count', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='topsql_cputime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('executions', models.BigIntegerField(blank=True)),
                ('cpu_time', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='topsql_diskread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('executions', models.BigIntegerField(blank=True)),
                ('disk_read', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='topsql_elapsedtime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('executions', models.BigIntegerField(blank=True)),
                ('elapsed_time', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='topsql_sharablememo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('executions', models.BigIntegerField(blank=True)),
                ('sharable_mem', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='topsql_sorts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('executions', models.BigIntegerField(blank=True)),
                ('sorts', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='topsql_version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('sql_id', models.CharField(max_length=50)),
                ('executions', models.BigIntegerField(blank=True)),
                ('version_count', models.BigIntegerField(blank=True)),
                ('module', models.CharField(max_length=65)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
