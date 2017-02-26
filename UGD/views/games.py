from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin

from ..models import Pairing
from ..tables import GamesTable
# todo Незакончено


class GamesView(SingleTableMixin, TemplateView):
    template_name = 'UGD/games.html'
    table_class = GamesTable
    table_pagination = {"per_page":50}

    def get_table_data(self):
        return Pairing.objects.filter(
            tournament_player_opponent__isnull=False,
            technical_result=False,
            round_skip=False
        ).order_by(
            '-tournament_player__tournament__date_begin',
            '-tournament_player__rating_start',
            '-tournament_player_opponent__rating_start'
        )

    def get_context_data(self, **kwargs):
        context = super(GamesView, self).get_context_data(**kwargs)
        return context
