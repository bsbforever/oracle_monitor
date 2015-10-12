# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0037_oraclelist_hit_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='sortusagetext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('tnsname', models.CharField(max_length=50)),
                ('sql_time', models.CharField(max_length=100)),
                ('logon', models.CharField(max_length=100)),
                ('osuser', models.CharField(max_length=50)),
                ('tablespace', models.CharField(max_length=50)),
                ('sql_text', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
