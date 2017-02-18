from functions import rate_calc_func

player_rating = 2368
opponents_rating = [
    (2414, 1),
    (2680, None),
    (2459, 1),
    (2548, 1),
    (2500, 1),
    (2561, 1),
    (2704, 0),
    # (2368, 1)
    ]

print('Корольов', player_rating)
print('Конечный рейтинг:', round(rate_calc_func.calculate_player_rating(player_rating, opponents_rating), 2))

player_rating = 2561
opponents_rating = [
    (2548, 1),
    (2500, 1),
    (2680, 1),
    (2704, 0),
    (2414, 0),
    (2472, 0),
    (2459, 1)
    # (2561, 1)
    ]
print('Жураковський')
print('Конечный рейтинг:', round(rate_calc_func.calculate_player_rating(player_rating, opponents_rating), 2))

player_rating = 2414
opponents_rating = [
    # (2414, 1),
    (2472, 0),
    (2459, 1),
    (2548, 1),
    (2500, 0),
    (2561, 1),
    (2704, 0),
    (2680, 0)
    ]
print('Крушельницький')
print('Конечный рейтинг:', round(rate_calc_func.calculate_player_rating(player_rating, opponents_rating), 2))

player_rating = 2704
opponents_rating = [
    (2459, 1),
    (2548, 1),
    (2500, 1),
    (2561, 1),
    (2680, 1),
    (2414, 1),
    (2472, 1)
    # (2704, 0)
    ]
print('Качановський')
print('Конечный рейтинг:', round(rate_calc_func.calculate_player_rating(player_rating, opponents_rating), 2))
