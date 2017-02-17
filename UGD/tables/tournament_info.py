import django_tables2 as tables
from django_tables2.utils import A
from ..models import TournamentPlayer


class TournamentInfoTable(tables.Table):
    place = tables.Column(
        verbose_name="Місце",
        attrs={"td": {"class": "col-xs-auto"}}
    )
    player = tables.LinkColumn(
        verbose_name="Прізвище та ім'я",
        viewname='UGD:player_info',
        args=[A('player_id')],
        attrs={"td": {"class": "col-lg-auto"}}
    )
    rank = tables.Column(
        verbose_name="Ранг",
        attrs={"td": {"class": "col-md-auto"}}
    )
    get_rating_start = tables.Column(
        verbose_name="R1",
        attrs={"td": {"class": "col-md-auto"}}
    )
    get_rating_finish = tables.Column(
        verbose_name="R2",
        attrs={"td": {"class": "col-md-auto"}}
    )
    get_result = tables.Column(
        verbose_name="Перемог",
        attrs={"td": {"class": "col-md-auto"}}
    )
    get_rating_delta = tables.Column(
        verbose_name="ΔR",
        attrs={"td": {"class": "col-md-auto"}}
    )

    orderable = False

    class Meta:
        model = TournamentPlayer
        order_by = 'place'
        fields = (
            'place',
            'player',
            'rank',
            'get_rating_start',
            'get_rating_finish',
            'get_result',
            'get_rating_delta'
        )
        attrs = {
            'id': 'tournament_info_table',
            'class': 'ugd_table'
        }
