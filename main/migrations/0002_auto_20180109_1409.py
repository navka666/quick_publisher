# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
        migrations.AddField(
            model_name='user',
            name='verfication_uunid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Uniaue Verification UUID'),
        ),
    ]
