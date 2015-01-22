# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_stretch', '0002_auto_20141202_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stretch_attempts',
            name='answerL',
            field=models.CharField(default='false', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stretch_attempts',
            name='answerN',
            field=models.CharField(default='false', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stretch_attempts',
            name='answerS',
            field=models.CharField(default='false', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stretch_attempts',
            name='user',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stretch_tasks',
            name='user',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
