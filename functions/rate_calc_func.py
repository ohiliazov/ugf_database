"""
    Данный модуль предназначен для расчета рейтинга по методу В.Корсака.
    Методика отличается от системы расчета рейтинга двумя моментами:
        1. В отличие от ЕГД вместо параметра е используется коэффциент развития при расчете нового рейтинга.
        2. Рейтинг каждого тура считается исходя из рейтинга полученного после расчета предыдущего тура.
    Более подробное описание здесь: http://forum.ufgo.org/viewtopic.php?f=3&t=1260
"""


from math import exp


def con(rate):
    rate = int(rate)
    res = 0
    if 100 <= rate < 200:
        res = 116 - ((rate - 100) * 3 / 50)
    elif 200 <= rate < 1300:
        res = 110 - ((rate - 200) * 1 / 20)
    elif 1300 <= rate < 2000:
        res = 55 - ((rate - 1300) * 1 / 25)
    elif 2000 <= rate < 2400:
        res = 27 - ((rate - 2000) * 3 / 100)
    elif 2400 <= rate < 2600:
        res = 15 - ((rate - 2400) * 1 / 50)
    elif 2600 <= rate < 2700:
        res = 11 - ((rate - 2600) * 1 / 100)
    elif rate >= 2700:
        res = 10
    return res


def a_param(rate):
    res = 0
    if 100 <= rate < 2700:
        res = 200 - ((rate - 100) * 130 / 2600)
    elif rate >= 2700:
        res = 70
    return res


def winning_expectancy(rate1, rate2, e_param=0):
    higher_rate, lower_rate = max(rate1, rate2), min(rate1, rate2)
    lower_win_exp = 1 / (exp((higher_rate - lower_rate) / a_param(lower_rate)) + 1)
    higher_win_exp = 1 - e_param - lower_win_exp
    if rate1 <= rate2:
        return lower_win_exp
    else:
        return higher_win_exp


def abnormal_growth(self_rate, number_of_rounds):
    return number_of_rounds * con(self_rate) * (0.45 + (3100 - self_rate) / 50000)


def abnormal_rating(self_rate, number_of_rounds):
    return self_rate + abnormal_growth(self_rate, number_of_rounds)


def growth(self_rate, opponent_rate, result=1):
    return con(self_rate) * (result - winning_expectancy(self_rate, opponent_rate) + (3100 - self_rate) / 50000)


def new_rating(self_rate, opponent_rate, result=1):
    return self_rate + growth(self_rate, opponent_rate, result)


def calculate_tournament_results(total_rounds, start_ratings, tournament_data):
    rated_rounds = {}
    finish_ratings = dict(start_ratings)

    for player in tournament_data:
        rounds_count = 0
        for pairing in tournament_data[player]:
            if pairing[1] in [0,1]:
                rounds_count += 1
                rated_rounds[player] = rounds_count

    for i in range(total_rounds):
        for player in finish_ratings:
            self_rate = finish_ratings[player]
            opponent_rate = finish_ratings[tournament_data[player][i][0]]
            result = tournament_data[player][i][1]
            if result not in [0, 1]:
                continue
            self_rate_2 = new_rating(self_rate, opponent_rate, result)
            finish_ratings[player] = self_rate_2
    abnormal_counter = 0
    for player in start_ratings:
        if finish_ratings[player] > abnormal_rating(start_ratings[player], rated_rounds[player]):
            abnormal_counter += 1
            start_ratings[player] = finish_ratings[player]
    if abnormal_counter:
        return calculate_tournament_results(total_rounds, start_ratings, tournament_data)
    else:
        return finish_ratings
