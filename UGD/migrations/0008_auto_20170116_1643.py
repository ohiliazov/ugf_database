# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UGD', '0007_auto_20170115_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_round', models.PositiveIntegerField(verbose_name='раунд')),
                ('color', models.BooleanField(default=False, verbose_name='колір')),
                ('handicap', models.PositiveIntegerField(choices=[(0, 'Без фори'), (1, 'Комі 0.5 очок'), (2, '2 камня'), (3, '3 камня'), (4, '4 камня'), (5, '5 каменів'), (6, '6 каменів'), (7, '7 каменів'), (8, '8 каменів'), (9, '9 каменів')], default=0, verbose_name='гандікап')),
                ('winner_color', models.NullBooleanField(default=None, verbose_name='колір переможця')),
                ('technical_win', models.BooleanField(default=False, verbose_name='технічна перемога')),
                ('game_record', models.FileField(blank=True, null=True, upload_to='uploads/game_records/')),
            ],
        ),
        migrations.CreateModel(
            name='TournamentPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.PositiveIntegerField(blank=True, null=True, verbose_name='місце')),
                ('rating_start', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='рейтинг-1')),
                ('rating_finish', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='рейтинг-2')),
                ('egd_rating_start', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='рейтинг EGD-1')),
                ('egd_rating_finish', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='рейтинг EGD-2')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UGD.Player', verbose_name='гравець')),
                ('rank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UGD.Rank', verbose_name='ранг')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UGD.Tournament', verbose_name='турнір')),
            ],
        ),
        migrations.AddField(
            model_name='pairing',
            name='player_black',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_black', to='UGD.TournamentPlayer', verbose_name='чорні'),
        ),
        migrations.AddField(
            model_name='pairing',
            name='player_white',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_white', to='UGD.TournamentPlayer', verbose_name='білі'),
        ),
    ]
