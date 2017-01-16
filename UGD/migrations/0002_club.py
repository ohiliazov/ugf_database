# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UGD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='назва міста')),
                ('egd_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='місто в EGD')),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UGD.Country', verbose_name='країна')),
            ],
            options={
                'verbose_name': 'місто',
                'verbose_name_plural': 'міста',
            },
        ),
    ]
