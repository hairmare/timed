# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employments', to='employment.Location'),
        ),
    ]
