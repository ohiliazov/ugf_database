from django.views.generic import TemplateView
# Create your views here.


import plotly.offline as opy
import plotly.graph_objs as go


class PlayerInfoView(TemplateView):
    template_name = 'UGD/player_info.html'

    def get_context_data(self, **kwargs):
        context = super(PlayerInfoView, self).get_context_data(**kwargs)

        x = [-2, 0, 4, 6, 7]
        y = [q ** 2 - q + 3 for q in x]
        trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
                            mode="lines", name='1st Trace')

        data = go.Data([trace1])
        layout = go.Layout(title="Meine Daten", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context
