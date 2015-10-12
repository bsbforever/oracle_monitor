# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0018_auto_20150129_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='topsql',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('top_type', models.CharField(max_length=50)),
                ('sql_text', models.CharField(max_length=100)),
                ('total', models.BigIntegerField()),
                ('executions', models.BigIntegerField()),
                ('rate', models.FloatField()),
                ('hash_vaule', models.CharField(max_length=50)),
                ('top_num', models.IntegerField()),
                ('sql_time', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
