# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170723_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
