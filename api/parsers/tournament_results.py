import re


def create_list_of_players(data):
    list_of_players = {}
    for row in data:
        list_of_players[data[row][0]] = row
    return list_of_players


def create_results(data):
    list_of_results = []
    player_list = create_list_of_players(data)
    for row in player_list:
        count = 0
        for game in data[player_list[row]][1]:
            count += 1
            if not re.match(r"(?P<place>[\d]+)+(?P<result>[+-]+)+(/(?P<color>[bw]+)+(?P<handicap>[\d]+)+)+", game):
                continue
            res = re.match(r"(?P<place>[\d]+)+(?P<result>[+-]+)+(/(?P<color>[bw]+)+(?P<handicap>[\d]+)+)+", game)
            try:
                player_list[res.group('place')]
            except KeyError:
                continue
            opponent = player_list[res.group('place')]
            if res.group('color') == 'b':
                black = player_list[row]
                white = opponent
                if res.group('result') == '+':
                    result = False
                else:
                    result = True
            else:
                black = opponent
                white = player_list[row]
                if res.group('result') == '-':
                    result = False
                else:
                    result = True
            list_of_results.append([count, black, white, result])
    return list_of_results
