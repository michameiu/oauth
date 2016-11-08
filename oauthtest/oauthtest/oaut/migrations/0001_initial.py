# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Envelope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_code', models.CharField(max_length=32)),
                ('date_due', models.DateTimeField()),
                ('exam_start', models.DateTimeField()),
                ('exam_duration', models.IntegerField(default=90)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
