"""
    Данный модуль предназначен для расчета рейтинга по методу В.Корсака.
    Методика отличается от системы EGD двумя моментами:
        1. В отличие от ЕГД вместо параметра е используется коэффциент развития при расчете нового рейтинга.
        2. Рейтинг каждого тура считается исходя из рейтинга полученного после расчета предыдущего тура.
    Более подробное описание здесь: http://forum.ufgo.org/viewtopic.php?f=3&t=1260
"""

from math import exp


def k_factor(rate: float):
    """
    Returns the K-factor for given rating
    :param rate: float >= 100
    :return: 10 <= float <= 122
    """
    res = 0
    if 100 <= rate < 200:
        res = 122 - rate * 0.06
    elif 200 <= rate < 1300:
        res = 120 - rate * 0.05
    elif 1300 <= rate < 2000:
        res = 107 - rate * 0.04
    elif 2000 <= rate < 2400:
        res = 87 - rate * 0.03
    elif 2400 <= rate < 2600:
        res = 63 - rate * 0.02
    elif 2600 <= rate < 2700:
        res = 37 - rate * 0.01
    elif rate >= 2700:
        res = 10
    return res


def a_factor(rate: float):
    """
    Returns A-factor for given rating
    :param rate: float >= 100
    :return: 70 <= float <= 200
    """
    res = 0
    if 100 <= rate < 2700:
        res = 205 - rate / 20
    elif rate >= 2700:
        res = 70
    return res


def winning_expectancy(player_rating: float, opponent_rating: float):
    """
    Returns the winning expectancy of player.
    :param player_rating: float >= 100
    :param opponent_rating: float >= 100
    :return: 0 <= float <= 1
    """
    lower_win_exp = 1 / (exp(abs(player_rating - opponent_rating) / a_factor(min(player_rating, opponent_rating))) + 1)
    if player_rating <= opponent_rating:
        return lower_win_exp
    else:
        return 1 - lower_win_exp


def abnormal_growth(player_rating: float, number_of_rounds: int):
    """
    Returns abnormal growth for a player within given number of rounds.
    :param player_rating: float >= 100
    :param number_of_rounds: int > 0
    :return: float >= self_rate
    """
    return number_of_rounds * k_factor(player_rating) * (0.45 + (3100 - player_rating) / 50000)


def abnormal_rating(player_rating: float, number_of_rounds: int):
    """
    Returns abnormal rating for a player within given number of rounds.
    :param player_rating: float >= 100
    :param number_of_rounds: int > 0
    :return:
    """
    return player_rating + abnormal_growth(player_rating, number_of_rounds)


def growth(player_rating: float, opponent_rating: float, result=1):
    """
    Returns growth for a player within given opponent and result.
    :param player_rating: float >= 100
    :param opponent_rating: float >= 100
    :param result: [0, 0.5, 1]
    :return: float
    """
    if result in [0, 0.5, 1]:
        return k_factor(player_rating) * (
            result - winning_expectancy(player_rating, opponent_rating) + (3100 - player_rating) / 50000)
    else:
        return 0


def new_rating(player_rating: float, opponent_rating: float, result=1):
    """
    Returns rating for a player within given opponent and result.
    :param player_rating: float >= 100
    :param opponent_rating: float >= 100
    :param result: [0, 0.5, 1]
    :return: float
    """
    next_rating = player_rating + growth(player_rating, opponent_rating, result)
    if next_rating < 100:
        next_rating = 100
    return next_rating


def count_rated_rounds(tournament_data):
    rated_rounds = dict()
    for player in tournament_data:
        rounds_count = 0
        for pairing in tournament_data[player]:
            if pairing[1] in [0, 0.5, 1]:
                rounds_count += 1
        rated_rounds[player] = rounds_count
    return rated_rounds


def count_round_results(current_ratings: dict, round_data: dict):
    round_ratings = current_ratings.copy()

    for player in round_data:
        player_rating = current_ratings[player]
        opponent_rating = current_ratings[round_data[player][0]]
        result = round_data[player][1]

        if result not in [0, 0.5, 1]:
            continue

        next_rating = new_rating(player_rating, opponent_rating, result)

        if next_rating < 100:
            next_rating = 100
        round_ratings[player] = next_rating

    return round_ratings


def calculate_tournament(initial_ratings: dict, tournament_data: dict):
    rounds = list(tournament_data[1]).__len__()
    rated_rounds = count_rated_rounds(tournament_data)
    finish_ratings = initial_ratings.copy()
    for current_round in range(rounds):
        round_data = {}
        for player in tournament_data:
            round_data[player] = tournament_data[player][current_round]
        finish_ratings = count_round_results(finish_ratings, round_data)

    abnormal_counter = 0
    abnormal_data = {}

    for player in initial_ratings:

        if finish_ratings[player] > abnormal_rating(initial_ratings[player], rated_rounds[player]):
            abnormal_data[player] = finish_ratings[player]
            abnormal_counter += 1
        else:
            abnormal_data[player] = initial_ratings[player]

    if abnormal_counter:
        return calculate_tournament(abnormal_data, tournament_data)
    else:
        return finish_ratings