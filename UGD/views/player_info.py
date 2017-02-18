from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin

from ..models import Player, TournamentPlayer
from ..tables import PlayerInfoTournamentTable
# todo Незакончено


class PlayerInfoView(SingleTableMixin, TemplateView):
    template_name = 'UGD/player_info.html'
    table_class = PlayerInfoTournamentTable
    table_pagination = False

    def get_table_data(self):
        return TournamentPlayer.objects.filter(player=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PlayerInfoView, self).get_context_data(**kwargs)
        context['player'] = Player.objects.get(pk=self.kwargs['pk'])
        return context
