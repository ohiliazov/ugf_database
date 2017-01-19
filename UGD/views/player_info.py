from django.views.generic import TemplateView
from ..models.tournaments import Tournament
from ..models.players import Player
from ..models.games import TournamentPlayer
# Create your views here.


import plotly.offline as opy
import plotly.graph_objs as go


class PlayerInfoView(TemplateView):
    template_name = 'UGD/player_info.html'

    def get_context_data(self, **kwargs):
        context = super(PlayerInfoView, self).get_context_data(**kwargs)
        player = self.kwargs['pk']
        print(player)
        x = [tournament_player.tournament.date_begin for tournament_player in TournamentPlayer.objects.filter(player_id=self.kwargs['pk'])]
        y = [tournament_player.egd_rating_start for tournament_player in TournamentPlayer.objects.filter(player_id=self.kwargs['pk'])]
        z = [tournament_player.egd_rating_finish for tournament_player in TournamentPlayer.objects.filter(player_id=self.kwargs['pk'])]
        f = [tournament_player.egd_rating_finish - tournament_player.egd_rating_start for tournament_player in TournamentPlayer.objects.filter(player_id=self.kwargs['pk'])]
        trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 101, 'size': "10"},
                            mode="lines", name='1st Trace')
        trace2 = go.Scatter(x=x, y=z, marker={'color': 'blue', 'symbol': 104, 'size': "15"},
                            mode="lines", name='2st Trace')
        trace3 = go.Scatter(x=x, y=f, marker={'color': 'green', 'symbol': 104, 'size': "15"},
                            mode="markers", name='3st Trace')

        data = go.Data([trace1, trace2, trace3])
        layout = go.Layout(title=Player.objects.get(pk=player).last_name, xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context
