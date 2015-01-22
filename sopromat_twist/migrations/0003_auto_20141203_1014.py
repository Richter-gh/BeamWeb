# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_twist', '0002_auto_20141202_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twist_tasks',
            name='answerM',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twist_tasks',
            name='answerT',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
    ]
