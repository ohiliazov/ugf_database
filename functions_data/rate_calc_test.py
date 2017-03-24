from functions_data import rate_calc_func

total_rounds = 7

start_ratings = {
    1: 2704,
    2: 2680,
    3: 2368,
    4: 2561,
    5: 2414,
    6: 2548,
    7: 2500,
    8: 2459
}

tournament_data = {
    1: [(8, 1), (6, 1),    (7, 1), (4, 1), (2, 1), (5, 1), (3, 1)],
    2: [(7, 1), (3, None), (4, 0), (8, 1), (1, 0), (6, 1), (5, 1)],
    3: [(5, 1), (2, None), (8, 1), (6, 1), (7, 1), (4, 1), (1, 0)],
    4: [(6, 1), (7, 1),    (2, 1), (1, 0), (5, 0), (3, 0), (8, 1)],
    5: [(3, 0), (8, 1),    (6, 1), (7, 0), (4, 1), (1, 0), (2, 0)],
    6: [(4, 0), (1, 0),    (5, 0), (3, 0), (8, 1), (2, 0), (7, 1)],
    7: [(2, 0), (4, 0),    (1, 0), (5, 1), (3, 0), (8, 0), (6, 0)],
    8: [(1, 0), (5, 0),    (3, 0), (2, 0), (6, 0), (7, 1), (4, 0)]
}

finish_ratings = rate_calc_func.calculate_tournament(start_ratings, tournament_data)
print(finish_ratings)
# for line in finish_ratings:
#     print(line, round(start_ratings[line]), round(finish_ratings[line]))
