# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_stretch', '0003_auto_20141202_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stretch_tasks',
            name='answerL',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stretch_tasks',
            name='answerN',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stretch_tasks',
            name='answerS',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
    ]
