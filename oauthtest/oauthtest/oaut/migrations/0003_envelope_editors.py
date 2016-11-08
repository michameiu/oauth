# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oaut', '0002_envelope_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='envelope',
            name='editors',
            field=models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL),
        ),
    ]
