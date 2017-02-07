from . import rate_calc_func

player_rating = 2150
rating_after = player_rating
opponents_rating = [
    (1618, 1),
    (1798, 1),
    (2115, 1),
    (2387, 0),
    (1514, 1)
    ]
print('Гилязов Александр')
print('Начальный рейтинг:', player_rating)
print('Конечный рейтинг:', round(rate_calc_func.calculate_player_rating(player_rating, opponents_rating), 2))
