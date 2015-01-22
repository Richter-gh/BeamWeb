# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_beam', '0002_beam_tasks_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beam_attempts',
            name='answerM',
            field=models.DecimalField(decimal_places=3, null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_attempts',
            name='answerQ',
            field=models.DecimalField(decimal_places=3, null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_tasks',
            name='answerM',
            field=models.DecimalField(decimal_places=3, null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_tasks',
            name='answerQ',
            field=models.DecimalField(decimal_places=3, null=True, max_digits=6),
            preserve_default=True,
        ),
    ]
