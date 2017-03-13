from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin

from ..models import Player, Tournament, TournamentPlayer
from ..plots import rating_history_plot
from ..tables import PlayerInfoTournamentTable, TournamentInfoTable


class PlayerInfoView(SingleTableMixin, TemplateView):
    """
    Информация про игрока
    """
    template_name = 'UGD/player_info.html'
    table_pagination = False
    table_class = PlayerInfoTournamentTable

    def get_table_data(self):
        return TournamentPlayer.objects.filter(player=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PlayerInfoView, self).get_context_data(**kwargs)
        context['player'] = Player.objects.get(pk=self.kwargs['pk'])
        context['rating_history_plot'] = rating_history_plot(self.kwargs['pk'])
        return context


class TournamentInfoView(SingleTableMixin, TemplateView):
    """
    Информация про турнир
    """
    template_name = 'UGD/tournament_info.html'
    table_pagination = False
    table_class = TournamentInfoTable

    def get_table_data(self):
        return TournamentPlayer.objects.filter(tournament=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(TournamentInfoView, self).get_context_data(**kwargs)
        context['tournament'] = Tournament.objects.get(pk=self.kwargs['pk'])
        return context
