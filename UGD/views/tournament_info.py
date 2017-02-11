from django.views.generic import TemplateView
from ..charts.rating_history import player_rating_history
# todo Незакончено


###
class TournamentInfoView(TemplateView):
    template_name = 'UGD/tournament_info.html'

    def get_context_data(self, **kwargs):
        context = super(TournamentInfoView, self).get_context_data(**kwargs)
        context['graph'] = player_rating_history(self.kwargs['pk'])
        return context
###
