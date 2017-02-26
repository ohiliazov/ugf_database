import django_tables2 as tables
from django_tables2.utils import A
from ..models import Pairing


class GamesTable(tables.Table):
    date_begin = tables.Column(
        verbose_name="Дата",
        accessor="tournament_player.tournament.date_begin"
    )
    tournament = tables.Column(
        verbose_name="Турнір",
        accessor="tournament_player.tournament"
    )
    tournament_player = tables.Column(
        verbose_name="Гравець",
        accessor="tournament_player.player"
    )
    tournament_player_opponent = tables.Column(
        verbose_name="Суперник",
        accessor="tournament_player_opponent.player"
    )
    game_result = tables.BooleanColumn(
        verbose_name="Перемога"
    )

    class Meta:
        model = Pairing
        fields = (
            'date_begin',
            'tournament',
            'tournament_player',
            'tournament_player_opponent',
            'game_result'
        )
        attrs = {
            'id': 'games_table',
            'class': 'ugd_table'
        }
        default = ''
