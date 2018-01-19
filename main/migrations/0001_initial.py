# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(unique=True, verbose_name='email', max_length=254)),
                ('full_name', models.CharField(null=True, verbose_name='full name', max_length=400, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', default=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', main.models.UserAccountManager()),
            ],
        ),
    ]
