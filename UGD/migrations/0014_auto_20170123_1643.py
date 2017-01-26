# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-01-23 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UGD', '0013_auto_20170123_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pairing',
            options={'verbose_name': 'результат партії', 'verbose_name_plural': 'результати партії'},
        ),
        migrations.AlterModelOptions(
            name='tournamentplayer',
            options={'verbose_name': 'учасник турніру', 'verbose_name_plural': 'учасники турніру'},
        ),
        migrations.RemoveField(
            model_name='pairing',
            name='player_black',
        ),
        migrations.RemoveField(
            model_name='pairing',
            name='player_white',
        ),
        migrations.RemoveField(
            model_name='pairing',
            name='technical_win',
        ),
        migrations.RemoveField(
            model_name='pairing',
            name='winner_color',
        ),
        migrations.AddField(
            model_name='pairing',
            name='game_result',
            field=models.BooleanField(default=False, verbose_name='перемога'),
        ),
        migrations.AddField(
            model_name='pairing',
            name='technical_result',
            field=models.BooleanField(default=False, verbose_name='технічний результат'),
        ),
        migrations.AddField(
            model_name='pairing',
            name='tournament_player',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tournament_player', to='UGD.TournamentPlayer', verbose_name='гравець'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pairing',
            name='tournament_player_opponent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tournament_player_opponent', to='UGD.TournamentPlayer', verbose_name='суперник'),
        ),
        migrations.AlterField(
            model_name='pairing',
            name='color',
            field=models.NullBooleanField(choices=[(None, 'Невідомо'), (False, 'Чорні'), (True, 'Білі')], default=None, verbose_name='колір'),
        ),
    ]
