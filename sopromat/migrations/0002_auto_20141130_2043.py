# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='beam_attempts',
        ),
        migrations.DeleteModel(
            name='beam_tasks',
        ),
    ]
