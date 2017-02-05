from django.http import HttpResponse, JsonResponse
from UGD.models.tournaments import Tournament
import re
# todo Добавить загрузку участников и результатов

INFO_TAGS = [
    'DT', 'PC', 'TC', 'EV'
]


def upload_egd_tournament(request):
    file = request.body.decode().split(sep="\n")
    tournament_data, tournament_head = [], {}
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
    return HttpResponse(tournament_head['EV']+' uploaded')
