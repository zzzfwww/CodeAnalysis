# -*- coding: utf-8 -*-
#  Copyright (c) 2021-2024 THL A29 Limited
#  #
#  This source code file is made available under MIT License
#  See LICENSE for details
#  ==============================================================================
# Generated by Django 3.1.14 on 2022-05-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan_conf', '0002_auto_20220422_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toollibscheme',
            name='condition',
            field=models.CharField(blank=True, help_text='条件', max_length=128, null=True),
        ),
    ]
