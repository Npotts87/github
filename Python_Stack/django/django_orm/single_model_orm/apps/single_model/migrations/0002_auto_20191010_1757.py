# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-10 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='eamil_address',
            new_name='email_address',
        ),
    ]