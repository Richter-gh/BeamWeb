# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_beam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beam_tasks',
            name='user',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
