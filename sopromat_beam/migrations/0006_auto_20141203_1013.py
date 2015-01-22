# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_beam', '0005_auto_20141202_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beam_tasks',
            name='answerM',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beam_tasks',
            name='answerQ',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
    ]
