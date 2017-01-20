import re
import zipfile
from UGD.models.tournaments import Tournament
from UGD.models.games import TournamentPlayer, Pairing


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
    print(results)
    return results


def upload_tournament(request):
    zip_file = zipfile.ZipFile('D:/Python/ugf_database/api/parsers/files/egd_tables.zip')
    file = zip_file.open('egd_tables/T161124A.h9').readlines()
    data = tournament_info(file)
    update_tournament(data)
    result_data = tournament_result(file)
    return data
