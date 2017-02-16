from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin

from ..models import Player
from ..tables import PlayerTable


# Create your views here.
class RatingListView(SingleTableMixin, TemplateView):
    """
    Рейтинг-лист УФГО
    """
    table_class = PlayerTable
    table_pagination = False
    template_name = 'UGD/rating_list.html'

    def get_table_data(self):
        return Player.objects.filter(active=True).order_by('-rating')
