from django.views.generic import TemplateView
from django_tables2 import MultiTableMixin

from ..tables import PlayerTable
from ..models import Player, Tournament
# todo ЗАКОНЧИТЬ ГЛАВНУЮ СТРАНИЦУ


# Create your views here.
class IndexView(MultiTableMixin, TemplateView):
    """
    Рейтинг-лист УФГО
    """
    table_pagination = False
    template_name = 'UGD/rating_list.html'
    tables = [
        PlayerTable(Player.objects.all()[:10].order_by('-rating')),
    ]
