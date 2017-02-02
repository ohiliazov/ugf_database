from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from ..tables.rating_list import PlayerTable
from ..filters.rating_list import PlayersFilter
from ..models.players import Player


# Create your views here.
class RatingListView(SingleTableMixin, FilterView):
    """
    Рейтинг-лист УФГО
    """
    table_class = PlayerTable
    table_pagination = False
    template_name = 'UGD/rating_list.html'
    filterset_class = PlayersFilter

    def get_queryset(self):
        return Player.objects.filter(active=True)
