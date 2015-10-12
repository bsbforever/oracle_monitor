# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Content',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
