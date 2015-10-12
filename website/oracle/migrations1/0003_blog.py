# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0002_oraclelist_alertpath'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100, blank=True)),
                ('Content', DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9   ', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
