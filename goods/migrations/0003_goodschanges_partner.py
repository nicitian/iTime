# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-26 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
        ('goods', '0002_auto_20180525_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodschanges',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partner.Partner'),
        ),
    ]
