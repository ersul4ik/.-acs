# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20170509_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingaccess',
            name='coming',
            field=models.TimeField(blank=True, null=True, verbose_name='\u041f\u0440\u0438\u0448\u0435\u043b \u0432'),
        ),
    ]