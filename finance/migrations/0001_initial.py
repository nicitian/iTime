# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-12 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_auto_20180410_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_finance', models.IntegerField(default=0)),
                ('total_income', models.IntegerField(default=0)),
                ('total_cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='create time')),
                ('opration_type', models.CharField(choices=[('支出', '支出'), ('收入', '收入')], default='收入', max_length=100)),
                ('money', models.IntegerField(default=0)),
                ('remark', models.CharField(default='其他', max_length=200)),
                ('change_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Account')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Finance')),
            ],
        ),
    ]
