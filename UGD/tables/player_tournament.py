import django_tables2 as tables
from django_tables2.utils import A

from ..models.games import TournamentPlayer


class PlayerTournamentTable(tables.Table):
    tournament = tables.LinkColumn(
        verbose_name="Назва турніру",
        viewname='UGD:tournament_info',
        args=[A('pk')]
    )
    get_result = tables.Column(verbose_name="Перемог")
    get_rating_delta = tables.Column(verbose_name="ΔR")

    class Meta:
        model = TournamentPlayer
        order_by = '-tournament.date_begin'
        fields = (
            'tournament.date_begin',
            'tournament',
            'rank',
            'place',
            'rating_start',
            'rating_finish',
            'get_result',
            'get_rating_delta'
        )
        attrs = {
            'id': 'player_tournament_table',
            'class': 'ugd_table'
        }
