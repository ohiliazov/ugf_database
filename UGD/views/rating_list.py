from django_tables2 import MultiTableMixin
from ..tables.rating_list import PlayerTable
from ..models.players import Player
from django.views.generic import TemplateView


# Create your views here.
class RatingListView(MultiTableMixin, TemplateView):
    """
    Рейтинг-лист УФГО
    """
    table_pagination = False
    template_name = 'UGD/rating_list.html'
    tables = [
        PlayerTable(Player.objects.filter(rank__gte=28).order_by('-rating')),
        PlayerTable(Player.objects.filter(active=True, rank__lt=27, rank__gte=21).order_by('-rating')),
        PlayerTable(Player.objects.filter(active=True, rank__lt=21, rank__gte=17).order_by('-rating')),
        PlayerTable(Player.objects.filter(active=True, rank__lt=17, rank__gte=12).order_by('-rating')),
        PlayerTable(Player.objects.filter(active=True, rank__lt=12, rank__gte=7).order_by('-rating')),
        PlayerTable(Player.objects.filter(active=True, rank__lt=7).order_by('-rating'))
    ]
