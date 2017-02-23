import plotly.offline as opy
import plotly.graph_objs as go
from ..models import TournamentPlayer


def rating_history_plot(player):
    player_data = TournamentPlayer.objects.filter(player=player).order_by('tournament__date_begin')
    x = []
    y1 = []
    y2 = []
    y3 = [player_data.last().rating_finish] * len(player_data)

    for tournament in player_data:
        x.append(tournament.tournament.date_begin)
        y1.append(tournament.rating_start)
        y2.append(tournament.rating_finish)

    trace1 = go.Scatter(
        x=x,
        y=y1,
        marker={
            'color': 'red',
            'symbol': 0,
            'size': 5
        },
        mode="markers",
        name='Старт'
    )
    trace2 = go.Scatter(
        x=x,
        y=y2,
        line={
            'color': 'blue',
            'shape': 'spline',
            'smoothing': 0.5
        },
        mode="lines+markers",
        name='Фініш'
    )
    trace3 = go.Scatter(
        x=x,
        y=y3,
        line={
            'color': 'black',
            'dash': 'dash'
        },
        mode="lines",
        name='Поточний'
    )

    data = go.Data([trace1, trace2, trace3])
    layout = go.Layout(
        title="Історія зміну рейтингу",
        xaxis={'title': 'Дата'},
        yaxis={'title': 'Рейтинг'},
        plot_bgcolor="#eff4ef",
        paper_bgcolor="#eff4ef",
        hiddenlabels=True
    )
    figure = go.Figure(data=data, layout=layout)
    div = opy.plot(figure, show_link=False, auto_open=False, output_type='div')

    return div
