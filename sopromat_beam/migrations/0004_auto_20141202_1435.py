# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_beam', '0003_auto_20141201_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beam_attempts',
            name='answerM',
            field=models.CharField(default=datetime.datetime(2014, 12, 2, 11, 34, 43, 714257, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beam_attempts',
            name='answerQ',
            field=models.CharField(default=datetime.datetime(2014, 12, 2, 11, 35, 0, 442304, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
    ]
