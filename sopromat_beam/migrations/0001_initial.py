# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beam_attempts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=200)),
                ('taskid', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('answerM', models.DecimalField(decimal_places=3, max_digits=6)),
                ('answerQ', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='beam_tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=1000)),
                ('answerM', models.DecimalField(decimal_places=3, max_digits=6)),
                ('answerQ', models.DecimalField(decimal_places=3, max_digits=6)),
                ('imagelink', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
