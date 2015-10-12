# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0028_oracledglist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topsql',
            old_name='total',
            new_name='buffer_gets_count',
        ),
        migrations.RenameField(
            model_name='topsql',
            old_name='dbname',
            new_name='sql_id',
        ),
        migrations.RenameField(
            model_name='topsql',
            old_name='hash_vaule',
            new_name='tnsname',
        ),
        migrations.RemoveField(
            model_name='topsql',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='topsql',
            name='top_num',
        ),
        migrations.RemoveField(
            model_name='topsql',
            name='top_type',
        ),
        migrations.AddField(
            model_name='topsql',
            name='cpu_time',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topsql',
            name='disk_read',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topsql',
            name='elapsed_time',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topsql',
            name='ipaddress',
            field=models.GenericIPAddressField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topsql',
            name='module',
            field=models.CharField(default='sqlplus', max_length=65),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topsql',
            name='sharable_mem',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topsql',
            name='sorts',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topsql',
            name='version_count',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topsql',
            name='sql_text',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
    ]
