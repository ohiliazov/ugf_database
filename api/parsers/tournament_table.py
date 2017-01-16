import re
from tournaments.models import Tournament
from details.models import Participant, Pairing
from players.models import Player


def tournament_info(request):
    file = request.body.decode().split(sep="\n")
    tournament_data, tournament_head = [], {}
    for line in file:
        if re.match(r'^; [\w\W]', line):
            tournament_data.append(line.split(sep=" ", maxsplit=1)[1])
    for line in tournament_data:
        tree = re.match(r'(?P<tag>[A-Z]+)\[(?P<text>[\w\W]+)\]', line)
        tournament_head[tree.group('tag')] = tree.group('text')
    return tournament_head


def tournament_results(request):
    file = request.body.decode().split(sep="\n")
    tournament_data, results = [], {}
    for line in file:
        if re.match(r"^(?P<place>[0-9]+)\s(?P<last_name>[\w]+) (?P<first_name>[\w]+)\w\W", line):
            tournament_data.append(line)
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


def update_tournament_info(data):
    dates = data['DT'].split(sep=",")
    Tournament.objects.update_or_create(
        egf_code=data['TC'],
        defaults={
            'name': data['EV'],
            'date_begin': dates[0],
            'date_end': dates[1]
        }
    )


def update_tournament_results(data, results):
    tournament = Tournament.objects.get(egf_code=data['TC'])
    for line in sorted(results):
        player = Player.objects.get(egf_code=line)
        Participant.objects.update_or_create(
            tournament=tournament,
            participant=player,
            place=results[line][0]
        )
    for line in sorted(results):
        player = Player.objects.get(egf_code=line)
        participant = Participant.objects.get(
            tournament=tournament,
            participant=player
        )
        round_count = 1
        for pairing in sorted(results[line][1]):
            regex = re.match(
                r"(?P<opponent_place>[0-9]+)"
                r"(?P<result>[+-=]+)"
                r"/(?P<color>[bw]+)?"
                r"(?P<handicap>[0-9]+)?",
                pairing
            )
            print(
                regex.group('opponent_place'),
                regex.group('result'),
                regex.group('color'),
                regex.group('handicap')
            )
            if regex.group('opponent_place') == '0':
                player_black = participant
                player_white = None
                result = 'bye'
                print(player_black, player_white)
            elif regex.group('color') == 'b':
                player_black = participant
                player_white = Participant.objects.get(
                    tournament=tournament,
                    place=regex.group('opponent_place')
                )
                if regex.group('result') == '+':
                    result = 'b'
                elif regex.group('result') == '-':
                    result = 'w'
                print(player_black, player_white)
            else:
                player_white = participant
                player_black = Participant.objects.get(
                    tournament=tournament,
                    place=regex.group('opponent_place')
                )
                if regex.group('result') == '+':
                    result = 'w'
                elif regex.group('result') == '-':
                    result = 'b'
            if not result:
                result = 'nr'
            pair = Pairing.objects.update_or_create(
                player_black=player_black,
                player_white=player_white,
                result=result,
                color=True,
                tournament_round=round_count,
                handicap=regex.group('handicap')
            )
            round_count += 1
            print(pair)
