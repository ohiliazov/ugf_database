import django_tables2 as tables
from django_tables2.utils import A

from ..models.players import Player


class PlayerTable(tables.Table):
    full_name = tables.LinkColumn(
        accessor="__str__",
        verbose_name="Прізвище та ім'я",
        order_by="last_name",
        viewname='UGD:player_info',
        empty_values=(),
        args=[A('pk')]
    )
    local_rank = tables.Column(
        accessor="local_rank.abbreviate",
        order_by="id",
        verbose_name="Розряд"
    )
    place = tables.Column(
        verbose_name="№"
    )
    egd_pin = tables.LinkColumn(
        verbose_name="EGD",
        viewname="UGD:egd_link",
        args=[A('egd_pin')]
    )

    class Meta:
        model = Player
        fields = (
            'place',
            'full_name',
            'city',
            'rating',
            'rank',
            'local_rank',
            'egd_pin'
        )
        attrs = {
            'id': 'rating_list_table',
            'class': 'rating_list'
        }
