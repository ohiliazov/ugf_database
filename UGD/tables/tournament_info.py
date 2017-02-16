import django_tables2 as tables
from django_tables2.utils import A
from ..models import TournamentPlayer


class TournamentInfoTable(tables.Table):
    player = tables.LinkColumn(
        verbose_name="Прізвище та ім'я",
        viewname='UGD:player_info',
        args=[A('player_id')]
    )
    get_result = tables.Column(verbose_name="Перемог")
    get_rating_delta = tables.Column(verbose_name="ΔR")

    class Meta:
        model = TournamentPlayer
        order_by = 'place'
        fields = (
            'place',
            'player',
            'rank',
            'rating_start',
            'rating_finish',
            'get_result',
            'get_rating_delta'
        )
        attrs = {
            'id': 'tournament_info_table',
            'class': 'ugd_table'
        }
