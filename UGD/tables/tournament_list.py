import django_tables2 as tables
from django_tables2.utils import A
from ..models import Tournament


class TournamentTable(tables.Table):
    name = tables.LinkColumn(
        verbose_name="Назва турніру",
        viewname='UGD:tournament_info',
        args=[A('pk')]
    )
    egd_code = tables.LinkColumn(
        verbose_name="EGD",
        viewname="UGD:egd_tournament_link",
        args=[A('egd_code')]
    )

    class Meta:
        model = Tournament
        fields = (
            'date_begin',
            'name',
            'city',
            'egd_code'
        )
        attrs = {
            'id': 'tournament_list_table',
            'class': 'ugd_table'
        }
