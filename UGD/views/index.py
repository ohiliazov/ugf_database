from django.views.generic import TemplateView
from django_tables2 import MultiTableMixin

from ..tables import IndexPlayerTable, IndexTournamentTable
from ..models import Player, Tournament
# todo ЗАКОНЧИТЬ ГЛАВНУЮ СТРАНИЦУ


# Create your views here.
class IndexView(MultiTableMixin, TemplateView):
    """
    Рейтинг-лист УФГО
    """
    table_pagination = False
    template_name = 'UGD/index.html'
    tables = [
        IndexPlayerTable(Player.objects.order_by('-rating')[:10]),
        IndexTournamentTable(Tournament.objects.order_by('-date_begin')[:10])
    ]
