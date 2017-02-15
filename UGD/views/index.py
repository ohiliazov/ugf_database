from django_tables2 import MultiTableMixin
from ..tables.rating_list import PlayerTable
from ..models.players import Player
from django.views.generic import TemplateView
# todo ЗАКОНЧИТЬ ГЛАВНУЮ СТРАНИЦУ

# Create your views here.
class IndexView(MultiTableMixin, TemplateView):
    """
    Рейтинг-лист УФГО
    """
    table_pagination = False
    template_name = 'UGD/rating_list.html'
    tables = [
        PlayerTable(Player.objects.all().order_by('-rating')[:10]),
    ]