from functions import rate_calc_func

PLAYERS = {
    1: 2704,
    2: 2680,
    3: 2472,
    4: 2561,
    5: 2414,
    6: 2548,
    7: 2500,
    8: 2459
}

GAMES = {
    1: [(8, 1), (6, 1),    (7, 1), (4, 1), (2, 1), (5, 1), (3, 1)],
    2: [(7, 1), (3, None), (4, 0), (8, 1), (1, 0), (6, 1), (5, 1)],
    3: [(5, 1), (2, None), (8, 1), (6, 1), (7, 1), (4, 1), (1, 0)],
    4: [(6, 1), (7, 1),    (2, 1), (1, 0), (5, 0), (3, 0), (8, 1)],
    5: [(3, 0), (8, 1),    (6, 1), (7, 0), (4, 1), (1, 0), (2, 0)],
    6: [(4, 0), (1, 0),    (5, 0), (3, 0), (8, 1), (2, 0), (7, 1)],
    7: [(2, 0), (4, 0),    (1, 0), (5, 1), (3, 0), (8, 0), (6, 0)],
    8: [(1, 0), (5, 0),    (3, 0), (2, 0), (6, 0), (7, 1), (4, 0)]
}

TEMP_PLAYERS = PLAYERS

for i in range(0, 7):
    for player in TEMP_PLAYERS:
        self_rate = TEMP_PLAYERS[player]
        opponent_rate = TEMP_PLAYERS[GAMES[player][i][0]]
        result = GAMES[player][i][1]
        if result not in [0, 1]:
            continue
        self_rate_2 = rate_calc_func.new_rating(self_rate, opponent_rate, result)
        TEMP_PLAYERS[player] = self_rate_2

for player in TEMP_PLAYERS:
    print(player, TEMP_PLAYERS[player])