from django_tables2 import SingleTableMixin
from django.views.generic import TemplateView
from ..tables.tournament_list import TournamentTable
from ..models.tournaments import Tournament


# Create your views here.
class TournamentListView(SingleTableMixin, TemplateView):
    """
    Рейтинг-лист УФГО
    """
    table_class = TournamentTable
    table_pagination = False
    template_name = 'UGD/tournament_list.html'

    def get_table_data(self):
        return Tournament.objects.all().order_by('-date_begin')
