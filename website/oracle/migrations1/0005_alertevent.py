# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0004_auto_20141121_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='alertevent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oracle_name', models.CharField(max_length=50, blank=True)),
                ('problem', models.CharField(max_length=1000, blank=True)),
                ('eventdate', models.DateField(auto_now_add=True)),
                ('solution', models.CharField(max_length=1000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
