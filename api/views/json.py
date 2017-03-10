from django.http import JsonResponse

from UGD.models.players import Player


# Create your views here.


def player_list(request):
    players = Player.objects.filter(active=True)
    data = {}
    for player in players:
        data[player.pk] = (player.get_full_name(), player.rating)
    return JsonResponse(status=200, data=data)
