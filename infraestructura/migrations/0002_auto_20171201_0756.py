# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 12:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipo', '0002_auto_20171125_0829'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infraestructura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DHabitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('numero', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DHabitacion_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DHabitacion_modified_by', to=settings.AUTH_USER_MODEL)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_habitacion_sede', to='infraestructura.CSede')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_habitacion_tipo', to='tipo.Tipo')),
            ],
            options={
                'verbose_name': 'habitacion',
                'db_table': 'infraestructura_habitacion',
            },
        ),
        migrations.AlterUniqueTogether(
            name='dhabitacion',
            unique_together=set([('numero',), ('sede',)]),
        ),
    ]
