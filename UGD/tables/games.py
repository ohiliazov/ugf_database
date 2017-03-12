import django_tables2 as tables
from django_tables2.utils import A
from ..models import Pairing


class GamesTable(tables.Table):
    date_begin = tables.Column(
        verbose_name="Дата",
        accessor="pairing_player.tournament.date_begin"
    )
    tournament = tables.Column(
        verbose_name="Турнір",
        accessor="pairing_player.tournament"
    )
    pairing_player = tables.Column(
        verbose_name="Гравець",
        accessor="pairing_player.player"
    )
    pairing_opponent = tables.Column(
        verbose_name="Суперник",
        accessor="pairing_opponent.player"
    )
    game_result = tables.BooleanColumn(
        verbose_name="Перемога"
    )

    class Meta:
        model = Pairing
        fields = (
            'date_begin',
            'tournament',
            'pairing_player',
            'pairing_opponent',
            'game_result'
        )
        attrs = {
            'id': 'games_table',
            'class': 'ugd_table'
        }
        default = ''
