from django.http import HttpResponse
from UGD.models.games import TournamentPlayer
import re

INFO_TAGS = [
    'DT', 'PC', 'TC', 'EV'
]


def upload_egd_ratings(request):
    """
    Загружаем данные по шапке, участникам и результатам турнира
    :param request: турнирная таблица ЕБД
    :return: ответ в форме JSON
    """
    file = request.body.decode().split(sep="\n")

    count = 0
    # ЗАПИСЬ ШАПКИ ТУРНИРА
    for line in file:
        row = line.split(sep=';')
        try:
            tournament_player = TournamentPlayer.objects.get(player__egd_pin=row[0], tournament__egd_code=row[1])
        except TournamentPlayer.DoesNotExist:
            continue
        tournament_player.rating_start = row[2]
        tournament_player.rating_finish = row[3]
        tournament_player.save()
        print(tournament_player)
        if count > 10:
            break
    return HttpResponse("Bla-bla")
