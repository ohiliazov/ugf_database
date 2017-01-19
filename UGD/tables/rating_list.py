import django_tables2 as tables
from ..models.players import Player
from ..models.games import TournamentPlayer
import itertools


class PlayerTable(tables.Table):
    full_name = tables.Column(
        accessor="__str__",
        verbose_name="Прізвище та ім'я",
        order_by="last_name"
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
            'local_rank'
        )
        attrs = {'class': 'main'}
