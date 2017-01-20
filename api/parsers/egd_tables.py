import re
import zipfile
from UGD.models.tournaments import Tournament
from .tournament_results import create_results
from UGD.models.games import TournamentPlayer, Pairing
from UGD.models.players import Player


def tournament_info(file):
    tournament_data, tournament_head = [], {}
    for line in file:
        row = line.decode(encoding="UTF-8")
        if re.match(r'^; [\w\W]', row):
            tournament_data.append(row.split(sep=" ", maxsplit=1))
    for line in tournament_data:
        tree = re.match(r'(?P<tag>[A-Z]+)\[(?P<text>[\w\W]+)\]', line[1])
        tournament_head[tree.group('tag')] = tree.group('text')
    return tournament_head


def update_tournament(data):
    tournament = Tournament.objects.get(egd_code=data['TC'])
    tournament.egd_class = data['CL']
    tournament.egd_name = data['EV']
    tournament.save()


def tournament_result(file):
    tournament_data, results = [], {}
    for line in file:
        row = line.decode(encoding="UTF-8")
        if re.match(r"^(?P<place>[0-9]+)\s(?P<last_name>[\w]+) (?P<first_name>[\w]+)\w\W", row):
            tournament_data.append(row)
    print(tournament_data)
    for line in tournament_data:
        tree = re.match(
            r"^(?P<place>[0-9]+)(\s)+"
            r"(?P<last_name>[\w]+)(\s)+"
            r"(?P<first_name>[\w]+)(\s)+"
            r"(?P<rank>[\ddpk]+)(\s)+"
            r"(?P<country>[\w]+)(\s)+"
            r"(?P<club>[\w]+)(\s)+"
            r"(?P<points>(([\d.])+(\s)+)+)+"
            r"(?P<results>([\d]+[=+-]+(/[bw]+[\d]+)?[\s]+)+)+"
            r"\|+(?P<egf>[\d]+)",
            line
        )
        results[tree.group('egf')] = [tree.group('place'), tree.group('results').split()]
    return results


def update_results(tournament, results):
    for result in results:
        print(result)
        player_black = Player.objects.get_or_create(egd_pin=result[1])
        player_white = Player.objects.get_or_create(egd_pin=result[2])
        black = TournamentPlayer.objects.get_or_create(tournament=tournament, player=player_black[0])
        white = TournamentPlayer.objects.get_or_create(tournament=tournament, player=player_white[0])
        Pairing.objects.update_or_create(player_black=black[0], player_white=white[0], defaults={
            'tournament_round': result[0],
            'winner_color': result[3]
        })


def upload_tournament(request):
    zip_file = zipfile.ZipFile('D:/Python/ugf_database/api/parsers/files/egd_tables.zip')
    list_of_tournaments = open('D:/Python/ugf_database/api/parsers/files/egd_related_tournaments_list.csv')
    for name in list_of_tournaments:
        if name:
            print(name)
        file = zip_file.open("egd_tables/%s.h9" % name.split()[0]).readlines()
        data = tournament_info(file)
        tournament = Tournament.objects.get(egd_code=data['TC'])
        update_tournament(data)
        result_data = tournament_result(file)
        list_of_results = create_results(result_data)
        update_results(tournament, list_of_results)
