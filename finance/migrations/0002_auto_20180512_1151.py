# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-12 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financerecords',
            name='opration_type',
            field=models.CharField(choices=[('支出', '支出'), ('收入', '收入'), ('财务修改', '财务修改')], default='收入', max_length=100),
        ),
    ]
