import django_tables2 as tables
from ..models.players import Player
import itertools


class PlayerTable(tables.Table):
    full_name = tables.Column(
        accessor="__str__",
        verbose_name="Прізвище та ім'я",
        order_by="last_name"

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
        row_attrs = {
            'player_id': lambda player: player.pk,
            'onclick': lambda player: "location.href='/UGD/player/%d/'" % player.pk,
        }
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
