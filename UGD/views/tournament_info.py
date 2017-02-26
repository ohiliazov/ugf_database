from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin

from ..tables import TournamentInfoTable
from ..models import Tournament, TournamentPlayer


class TournamentInfoView(SingleTableMixin, TemplateView):
    template_name = 'UGD/tournament_info.html'
    table_class = TournamentInfoTable
    table_pagination = False

    def get_table_data(self):
        return TournamentPlayer.objects.filter(tournament=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(TournamentInfoView, self).get_context_data(**kwargs)
        context['tournament'] = Tournament.objects.get(pk=self.kwargs['pk'])
        return context
