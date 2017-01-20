import plotly.graph_objs as go
import plotly.offline as opy

import datetime
from ..models.games import TournamentPlayer


def player_rating_history(player_id):
    x = [tournament_player.tournament.date_begin for tournament_player in
         TournamentPlayer.objects.filter(player_id=player_id, tournament__date_begin__gte=datetime.datetime.now()-datetime.timedelta(days=720))]
    y = [tournament_player.egd_rating_start for tournament_player in
         TournamentPlayer.objects.filter(player_id=player_id, tournament__date_begin__gte=datetime.datetime.now()-datetime.timedelta(days=720))]
    z = [tournament_player.egd_rating_finish for tournament_player in
         TournamentPlayer.objects.filter(player_id=player_id, tournament__date_begin__gte=datetime.datetime.now()-datetime.timedelta(days=720))]

    rating_before = go.Scatter(x=x, y=y, marker={'color': 'blue', 'symbol': "square-dot", 'size': "10"},
                        mode="lines+markers", name='R1')
    rating_after = go.Scatter(x=x, y=z, marker={'color': 'red', 'symbol': "square-dot", 'size': "10"},
                        mode="lines+markers", name='R2', fill='tonexty', fillcolor="yellow")

    data = go.Data([rating_before, rating_after])
    layout = go.Layout()
    figure = go.Figure(data=data, layout=layout)
    graph = opy.plot(figure, output_type='div')
    return graph
