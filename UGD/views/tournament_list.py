from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from ..tables.tournament_list import TournamentTable
from ..filters.tournament_list import TournamentsFilter
from ..models.tournaments import Tournament


# Create your views here.
class TournamentListView(SingleTableMixin, FilterView):
    """
    Рейтинг-лист УФГО
    """
    table_class = TournamentTable
    table_pagination = False
    template_name = 'UGD/tournament_list.html'
    filterset_class = TournamentsFilter

    def get_queryset(self):
        return Tournament.objects.all().order_by('-date_begin')
