# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_stretch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stretch_attempts',
            name='answerM',
        ),
        migrations.RemoveField(
            model_name='stretch_attempts',
            name='answerQ',
        ),
        migrations.RemoveField(
            model_name='stretch_tasks',
            name='answerM',
        ),
        migrations.RemoveField(
            model_name='stretch_tasks',
            name='answerQ',
        ),
        migrations.AddField(
            model_name='stretch_attempts',
            name='answerL',
            field=models.CharField(max_length=1000, default=datetime.datetime(2014, 12, 2, 11, 52, 51, 131643, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stretch_attempts',
            name='answerN',
            field=models.CharField(max_length=1000, default=datetime.datetime(2014, 12, 2, 11, 52, 56, 470663, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stretch_attempts',
            name='answerS',
            field=models.CharField(max_length=1000, default=datetime.datetime(2014, 12, 2, 11, 53, 0, 201677, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stretch_tasks',
            name='answerL',
            field=models.DecimalField(decimal_places=3, null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stretch_tasks',
            name='answerN',
            field=models.DecimalField(decimal_places=3, null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stretch_tasks',
            name='answerS',
            field=models.DecimalField(decimal_places=3, null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stretch_tasks',
            name='user',
            field=models.CharField(max_length=200, default=datetime.datetime(2014, 12, 2, 11, 53, 14, 74709, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
