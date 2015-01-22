# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_twist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twist_attempts',
            name='answerQ',
        ),
        migrations.RemoveField(
            model_name='twist_tasks',
            name='answerQ',
        ),
        migrations.AddField(
            model_name='twist_attempts',
            name='answerT',
            field=models.CharField(default='false', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twist_tasks',
            name='answerT',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twist_tasks',
            name='user',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twist_attempts',
            name='answerM',
            field=models.CharField(default='false', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twist_attempts',
            name='date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twist_attempts',
            name='taskid',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twist_attempts',
            name='user',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twist_tasks',
            name='answerM',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twist_tasks',
            name='text',
            field=models.CharField(null=True, max_length=1000),
            preserve_default=True,
        ),
    ]
