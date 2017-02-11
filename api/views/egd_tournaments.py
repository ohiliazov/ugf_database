from django.http import HttpResponse
from UGD.models.tournaments import Tournament
from UGD.models.games import Player, TournamentPlayer
from UGD.models.ranks import Rank
import re
# todo Добавить загрузку участников и результатов

INFO_TAGS = [
    'DT', 'PC', 'TC', 'EV'
]


def upload_egd_tournament(request):
    file = request.body.decode().split(sep="\n")
    tournament_head = {}
    for line in file:
        tag = re.match(r"^; (?P<tag>[\w]+)+\[(?P<value>[\w\W]+)+\]", line)
        if tag and tag.group('tag') in INFO_TAGS:
            tournament_head[tag.group('tag')] = tag.group('value')
    tournament = Tournament.objects.update_or_create(egd_code=tournament_head['TC'])[0]
    tournament.name = tournament_head['EV']
    tournament_dates = tournament_head['DT'].split(sep=',')
    tournament.date_begin = tournament_dates[0]
    tournament.date_end = tournament_dates[1]
    tournament.save()
    print(tournament)
    count = 0
    for line in file:
        if line in ('',';',';.'):
            continue
        tag = re.match(
            r"^\s*(?P<place>[\d]+)(\s)+"                          # +Место в турнире
            r"(?P<last_name>[\w-]+)(\s)+"                        # +Фамилия
            r"(?P<first_name>[\w]+)(\s)+"                       # +Имя
            r"(?P<rank>[\d]+(d|p|k)+)(\s)+"                          # -Ранг
            r"(?P<country>[\w]+)(\s)+"                          # -Страна
            r"(?P<club>[\w]+)(\s)+"                             # -Город
            r"(?P<points>(([\d.])+(\s)+)+)*"                    # -Очки
            r"(?P<results>([\d]+(=|\+|-)+(/[bw]+[\d]?)?[\s]+)+)+"  # +Результаты партии
            r"\|(?P<egd_pin>[\d]+)",                           # +Код игрока в EGF
            line
        )
        if tag is not None:
            player = Player.objects.get_or_create(
                egd_pin=tag.group('egd_pin'),
                defaults={
                    "last_name": tag.group('last_name'),
                    "first_name": tag.group('first_name'),
                    "rank": Rank.objects.get(egd_grade=tag.group('rank'))
                }
            )[0]
            tournament_player = TournamentPlayer.objects.update_or_create(
                player=player,
                tournament=tournament,
                defaults={
                    "place": tag.group('place'),
                    "rank": Rank.objects.get(egd_grade=tag.group('rank'))
                }
            )
            count += 1
        elif re.match(r"^; (?P<tag>[\w]+)+\[(?P<value>[\w\W]+)+\]", line) is None:
            print(line, tag)
    return HttpResponse('%s uploaded - %d participants' % (tournament.name, count))
