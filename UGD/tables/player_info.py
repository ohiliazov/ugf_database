import django_tables2 as tables
from django_tables2.utils import A

from ..models import TournamentPlayer


class PlayerInfoTournamentTable(tables.Table):
    date_begin = tables.DateColumn(
        accessor="tournament.date_begin",
        format="d.m.Y",
        verbose_name="Дата",
        attrs={"td": {"class": "col-xs-auto"}}
    )
    tournament = tables.LinkColumn(
        accessor="tournament.name",
        verbose_name="Назва турніру",
        viewname='UGD:tournament_info',
        args=[A('tournament_id')],
        attrs={"td": {"class": "col-lg-auto"}}
    )
    rank = tables.Column(
        verbose_name="Ранг",
        attrs={"td": {"class": "col-md-auto"}}
    )
    get_rating_start = tables.Column(
        verbose_name="R1",
        attrs={"td": {"class": "col-md-auto"}},
        order_by="rating_start"
    )
    get_rating_finish = tables.Column(
        verbose_name="R2",
        attrs={"td": {"class": "col-md-auto"}},
        order_by="rating_finish"
    )
    get_result = tables.Column(
        verbose_name="Перемог",
        attrs={"td": {"class": "col-md-auto"}},
        orderable=False
    )
    get_rating_delta = tables.Column(
        verbose_name="ΔR",
        attrs={"td": {"class": "col-md-auto"}},
        orderable=False
    )

    class Meta:
        model = TournamentPlayer
        order_by = '-date_begin'
        fields = (
            'date_begin',
            'tournament',
            'rank',
            'place',
            'get_rating_start',
            'get_rating_finish',
            'get_result',
            'get_rating_delta'
        )
        attrs = {
            'id': 'player_info_tournament_table',
            'class': 'ugd_table'
        }
