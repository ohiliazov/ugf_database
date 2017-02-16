import django_tables2 as tables
from django_tables2.utils import A
from ..models import Player


class IndexPlayerTable(tables.Table):

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
    rating = tables.Column(
        verbose_name="Рейтинг",
        attrs={"td": {"class":"col-xs-auto"}}
    )
    rank = tables.Column(
        verbose_name="Ранг",
        attrs={"td": {"class": "col-md-auto"}}
    )

    class Meta:
        model = Player
        fields = (
            'place',
            'full_name',
            'rating',
            'rank'
        )
        attrs = {
            'id': 'index_player_table',
            'class': 'ugd_table'
        }
        default = ''
