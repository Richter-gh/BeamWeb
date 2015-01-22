# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sopromat_inertia', '0002_auto_20141202_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='inertia_attempts',
        ),
        migrations.DeleteModel(
            name='inertia_tasks',
        ),
    ]
