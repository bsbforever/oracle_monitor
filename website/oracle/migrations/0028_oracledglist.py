# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0027_mssqllist_hostname'),
    ]

    operations = [
        migrations.CreateModel(
            name='oracledglist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddress', models.GenericIPAddressField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('port', models.CharField(max_length=50)),
                ('tnsname', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=100)),
                ('monitor_type', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
