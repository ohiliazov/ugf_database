# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-02-24 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UGD', '0022_auto_20170224_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='рейтинг'),
        ),
    ]