# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oraclelist',
            fields=[
                ('ipaddress', models.GenericIPAddressField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('port', models.CharField(max_length=50)),
                ('tnsname', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
