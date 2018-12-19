# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_clinic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dentist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Dentist'),
        ),
    ]