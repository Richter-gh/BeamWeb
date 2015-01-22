# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_inertia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inertia_attempts',
            name='answerM',
        ),
        migrations.RemoveField(
            model_name='inertia_attempts',
            name='answerQ',
        ),
        migrations.RemoveField(
            model_name='inertia_tasks',
            name='answerM',
        ),
        migrations.RemoveField(
            model_name='inertia_tasks',
            name='answerQ',
        ),
        migrations.AddField(
            model_name='inertia_attempts',
            name='answerX',
            field=models.CharField(max_length=1000, default='false'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inertia_attempts',
            name='answerY',
            field=models.CharField(max_length=1000, default='false'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inertia_tasks',
            name='answerX',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inertia_tasks',
            name='answerY',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inertia_tasks',
            name='user',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inertia_attempts',
            name='date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inertia_attempts',
            name='taskid',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inertia_attempts',
            name='user',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inertia_tasks',
            name='text',
            field=models.CharField(null=True, max_length=1000),
            preserve_default=True,
        ),
    ]
