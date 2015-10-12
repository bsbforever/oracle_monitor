# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0005_alertevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='oraclestatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tnsname', models.CharField(max_length=100)),
                ('jobstatus', models.CharField(max_length=20)),
                ('alertstatus', models.CharField(max_length=20)),
                ('dbsize', models.CharField(max_length=50)),
                ('tbstatus', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
