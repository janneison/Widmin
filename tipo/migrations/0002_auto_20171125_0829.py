# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltipo',
            name='icono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='icono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
