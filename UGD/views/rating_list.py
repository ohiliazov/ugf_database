from django_tables2 import SingleTableMixin
from ..tables.rating_list import PlayerTable
from ..models.players import Player
from django.views.generic import TemplateView


# Create your views here.
class RatingListView(SingleTableMixin, TemplateView):
    """
    Рейтинг-лист УФГО
    """
    table_pagination = False
    template_name = 'UGD/rating_list.html'
    table_class = PlayerTable

    def get_table_data(self):
        return Player.objects.filter(active=True).order_by('-rating')
