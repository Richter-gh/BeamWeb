# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_beam', '0004_auto_20141202_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beam_attempts',
            name='answerM',
            field=models.CharField(max_length=1000, default='false'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_attempts',
            name='answerQ',
            field=models.CharField(max_length=1000, default='false'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_attempts',
            name='user',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_tasks',
            name='text',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_tasks',
            name='user',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
