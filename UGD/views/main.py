from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin, MultiTableMixin

from ..models import Player, Tournament, Pairing
from ..tables import IndexPlayerTable, IndexTournamentTable, PlayerTable, TournamentTable, GamesTable

"""
В этом файле содержится информация по главной странице, рейтинг-листу, списку турниров и партий.
"""


class IndexView(MultiTableMixin, TemplateView):
    """
    Головна сторінка
    """
    template_name = 'UGD/index.html'
    table_pagination = False
    tables = [
        IndexPlayerTable(Player.objects.order_by('-rating')[:10]),
        IndexTournamentTable(Tournament.objects.order_by('-date_begin')[:10])
    ]


class RatingListView(SingleTableMixin, TemplateView):
    """
    Рейтинг-лист
    """
    template_name = 'UGD/rating_list.html'
    table_pagination = False
    table_class = PlayerTable

    def get_table_data(self):
        return Player.objects.filter(active=True).order_by('-rating')


class TournamentListView(SingleTableMixin, TemplateView):
    """
    Турніри
    """
    table_class = TournamentTable
    table_pagination = False
    template_name = 'UGD/tournament_list.html'

    def get_table_data(self):
        return Tournament.objects.all().order_by('-date_begin')


# todo Незакончено
class PairingListView(SingleTableMixin, TemplateView):
    template_name = 'UGD/games.html'
    table_class = GamesTable
    table_pagination = {"per_page": 50}

    def get_table_data(self):
        return Pairing.objects.filter(
            pairing_opponent__isnull=False,
            technical_result=False,
            round_skip=False
        )

    def get_context_data(self, **kwargs):
        context = super(PairingListView, self).get_context_data(**kwargs)
        return context
