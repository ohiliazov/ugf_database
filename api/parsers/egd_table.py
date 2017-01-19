import re
import zipfile


def tournament_info(request):
    print(request.GET['egd_code'])
    zip_file = zipfile.ZipFile('D:/Python/ugf_database/api/parsers/files/egd_tables.zip')
    print(zip_file.namelist())
    file = zip_file.open('egd_tables/T161124A.h9').readlines()
    tournament_data, tournament_head = [], {}
    for line in file:
        row = line.decode(encoding="UTF-8")
        if re.match(r'^; [\w\W]', row):
            tournament_data.append(row.split(sep=" ", maxsplit=1))
    for line in tournament_data:
        tree = re.match(r'(?P<tag>[A-Z]+)\[(?P<text>[\w\W]+)\]', line[1])
        tournament_head[tree.group('tag')] = tree.group('text')
    for line in tournament_head:
        print(line, tournament_head[line])
