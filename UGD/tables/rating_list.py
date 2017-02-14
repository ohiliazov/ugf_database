import django_tables2 as tables
from django_tables2.utils import A
from ..models.players import Player


class PlayerTable(tables.Table):

    place = tables.Column(
        verbose_name="№",
        attrs={"td": {"class":"col-xs-auto"}}
    )
    full_name = tables.LinkColumn(
        accessor="__str__",
        verbose_name="Прізвище та ім'я",
        order_by="last_name",
        viewname='UGD:player_info',
        args=[A('pk')],
        attrs={"td": {"class":"col-lg-auto"}}
    )
    city = tables.Column(
        verbose_name="Місто",
        attrs={"td": {"class":"col-md-auto"}}
    )
    rating = tables.Column(
        verbose_name="Рейтинг",
        attrs={"td": {"class":"col-xs-auto"}}
    )
    rank = tables.Column(
        verbose_name="Ранг",
        attrs={"td": {"class": "col-md-auto"}}
    )
    local_rank = tables.Column(
        accessor="local_rank.abbreviate",
        order_by="local_rank.id",
        verbose_name="Розряд",
        attrs={"td": {"class":"col-md-auto"}}
    )
    egd_pin = tables.LinkColumn(
        verbose_name="EGD",
        viewname="UGD:egd_player_link",
        args=[A('egd_pin')],
        attrs={"td": {"class":"col-xs-auto"}}
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
            'class': 'ugd_table'
        }
        default = ''
