# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-14 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_auto_20191014_1723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ninjas',
            new_name='Ninja',
        ),
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.Dojo'),
        ),
    ]
