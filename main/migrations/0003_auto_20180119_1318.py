# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180109_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='verfication_uunid',
            new_name='verification_uunid',
        ),
    ]
