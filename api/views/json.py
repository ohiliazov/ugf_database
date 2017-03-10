from django.db.models import Q
from django.http import JsonResponse

from UGD.models.players import Player


# Create your views here.


def player_list(request):
    try:
        players = Player.objects.filter(Q(active=True),
                                        (Q(last_name__contains=request.GET['full_name']))
                                        | Q(first_name__contains=request.GET['full_name'])).order_by('-rating')
    except KeyError:
        players = Player.objects.filter(active=True).order_by('-rating')
    data = {}
    for player in players:
        data[player.pk] = (player.get_full_name(), player.rating)
    return JsonResponse(status=200, data=data)
