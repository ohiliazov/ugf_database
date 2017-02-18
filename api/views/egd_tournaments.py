from django.http import HttpResponse
from UGD.models.tournaments import Tournament
from UGD.models.players import Player
from UGD.models.games import TournamentPlayer, Pairing
from UGD.models.ranks import Rank
import re

INFO_TAGS = [
    'DT', 'PC', 'TC', 'EV'
]


def upload_egd_tournament(request):
    """
    Загружаем данные по шапке, участникам и результатам турнира
    :param request: турнирная таблица ЕБД
    :return: ответ в форме JSON
    """
    file = request.body.decode().split(sep="\n")

    tournament_head = {}
    tournament_results = {}
    count = 0

    # ЗАПИСЬ ШАПКИ ТУРНИРА
    for line in file:
        tag = re.match(r"^; (?P<tag>[\w]+)+\[(?P<value>[\w\W]+)+\]", line)
        if tag and tag.group('tag') in INFO_TAGS:
            tournament_head[tag.group('tag')] = tag.group('value')

    # Обновляем или создаем новую запись о турнире
    tournament = Tournament.objects.update_or_create(egd_code=tournament_head['TC'])[0]
    tournament.name = tournament_head['EV']
    tournament_dates = tournament_head['DT'].split(sep=',')
    tournament.date_begin = tournament_dates[0]
    tournament.date_end = tournament_dates[1]
    tournament.save()
    print(tournament)

    # ЗАПИСЬ УЧАСТНИКОВ ТУРНИРА
    for line in file:
        if line in (';', ';.', False):
            # Пропускаем пустые строки
            continue

        tag = re.match(
            r"^\s*(?P<place>[\d]+)(\s)+"                             # +Место в турнире
            r"(?P<last_name>[\w-]+)(\s)+(?P<first_name>[\w]+)(\s)+"  # +Полное имя
            r"(?P<rank>[\d]+(d|p|k)+)(\s)+"                          # +Ранг
            r"(?P<country>[\w]+)(\s)+(?P<club>[\w]+)(\s)+"           # -Страна и город
            r"(?P<points>(([\d.=])+(\s)+)+){0,5}"                         # -Очки
            r"(?P<results>([\d]+(=|\+|-)+(/[bw]+[\d]?)?[\s]+)+)+"    # +Результаты партии
            r"\|(?P<egd_pin>[\d]+)",                                 # +Код игрока в EGF
            line
        )

        if tag is not None:
            count += 1

            # Ищем или создаем игрока в базе данных
            player = Player.objects.get_or_create(
                egd_pin=tag.group('egd_pin'),
                defaults={
                    "last_name": tag.group('last_name'),
                    "first_name": tag.group('first_name'),
                    "rank": Rank.objects.get(egd_grade=tag.group('rank'))
                }
            )[0]

            # Обновляем или создаем участника турнира в базе данных
            tournament_player = TournamentPlayer.objects.update_or_create(
                player=player,
                tournament=tournament,
                defaults={
                    "place": tag.group('place'),
                    "rank": Rank.objects.get(egd_grade=tag.group('rank'))
                }
            )[0]

            # Добавляем информацию о игроке и результатах в справочник
            tournament_results[tag.group('place')] = [tournament_player, tag.group('results').split()]

        elif re.match(r"^; (?P<tag>[\w]+)+\[(?P<value>[\w\W]+)+\]", line) is None:
            print(line, tag)

    # ЗАПИСЬ РЕЗУЛЬТАТОВ ПАРТИЙ
    for place in tournament_results:
        round_count = 0
        for results in tournament_results[place][1]:
            round_count += 1
            result = re.match(
                r"(?P<opponent_place>\d+)"
                r"(?P<result>(=|\+|-)+)"
                r"(/(?P<player_color>(b|w|h)+)"
                r"(?P<handicap>\d?)?)?",
                results
            )

            if result.group('opponent_place') == '0':
                pairing = Pairing.objects.update_or_create(
                    tournament_player=tournament_results[place][0],
                    tournament_round=round_count
                )[0]
                pairing.round_skip = True

            else:
                pairing = Pairing.objects.update_or_create(
                    tournament_player=tournament_results[place][0],
                    tournament_player_opponent=tournament_results[result.group('opponent_place')][0],
                    tournament_round=round_count
                )[0]

            if result.group('result') == '+':
                pairing.game_result = True
            elif result.group('result') == '-':
                pairing.game_result = False
            else:
                pairing.game_result = None

            if result.group('player_color') == 'w':
                pairing.color = True
            elif result.group('player_color') == 'b':
                pairing.color = False
            else:
                pairing.color = None

            if result.group('handicap'):
                pairing.handicap = result.group('handicap')
            else:
                pairing.handicap = 0
            pairing.save()
    return HttpResponse('%s uploaded - %d participants' % (tournament.name, count))
