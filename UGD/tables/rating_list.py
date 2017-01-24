import django_tables2 as tables
from ..models.players import Player
from django_tables2.utils import A
import itertools


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
        verbose_name="Спортивний розряд",
        order_by="id"
    )
    rating = tables.Column(
        verbose_name="Рейтинг УФГО"
    )
    ufgo_member = tables.BooleanColumn(
        verbose_name="Член УФГО"
    )

    class Meta:
        model = Player
        fields = (
            'id',
            'full_name',
            'club',
            'rating',
            'rank',
            'local_rank',
            'ufgo_member'
        )
        attrs = {'class': 'main'}
