from django.db.models import Q
from django.http import JsonResponse

from UGD.models import Player


def json_rating_list(request):
    """
    Rating list
    :param request: POST may have full_name
    :return: JSON of matched players
    """
    rating_list_data = {}
    counter = 0
    all_players = Player.objects.filter(active=True)

    if request.is_ajax():
        try:
            all_players = all_players.filter(
                Q(last_name__contains=request.POST['full_name']) |
                Q(first_name__contains=request.POST['full_name'])
            )
        except KeyError:
            pass

        try:
            all_players = all_players.filter(city__name__contains=request.POST['city'])
        except KeyError:
            pass

    for player in all_players:
        counter += 1
        player_data = {
            'place': player.place,
            'full_name': player.get_full_name(),
            'city': player.get_city(),
            'rank': player.get_rank(),
            'rating': player.get_rating(),
            'local_rank': player.get_local_rank(),
            'sex': player.get_sex_display()
        }
        rating_list_data[counter] = player_data

    return JsonResponse(status=200, data=rating_list_data)
