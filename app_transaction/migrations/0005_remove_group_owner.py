# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-27 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0004_auto_20190227_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='owner',
        ),
    ]
