from math import exp, floor


def con(rate):
    
    """Вычисляем параметр con по данному рейтингу"""
    rate = int(rate)
    res = 0
    if 100 <= rate < 200:
        res = 116 - ((rate - 100)*3/50)
    elif 200 <= rate < 1300:
        res = 110 - ((rate - 200)*1/20)
    elif 1300 <= rate < 2000:
        res = 55 - ((rate - 1300)*1/25)
    elif 2000 <= rate < 2400:
        res = 27 - ((rate - 2000)*3/100)
    elif 2400 <= rate < 2600:
        res = 15 - ((rate - 2400)*1/50)
    elif 2600 <= rate < 2700:
        res = 11 - ((rate - 2600)*1/100)
    elif rate >= 2700:
        res = 10
    return res


def a_param(rate):
    
    """Вычисляем параметр a по данному рейтингу"""
    
    res = 0
    if 100 <= rate < 2700:
        res = 200 - ((rate - 100)*130/2600)
    elif rate >= 2700:
        res = 70
    return res


def winning_expectancy(rate1, rate2, e_param=0):
    
    """Вычисляем вероятность победы игрока над соперником"""
    higher_rate = max(rate1, rate2)
    lower_rate = min(rate1, rate2)
    lower_win_exp = 1 / (exp((higher_rate - lower_rate) / a_param(lower_rate)) + 1)
    higher_win_exp = 1 - e_param - lower_win_exp
    if rate1 <= rate2:
        return lower_win_exp
    else:
        return higher_win_exp


def abnormal_growth(self_rate, number_of_rounds):
    
    """Вычисляем аномальный рейтинг по данному рейтингу и количеству туров"""
    
    return number_of_rounds * con(self_rate) * (0.45 + (3100 - self_rate) / 50000)


def growth(self_rate, opponent_rate, result=1):
    
    """Вычисляем прирост рейтинга игрока по рейтингам соперников и результату"""
    return con(self_rate) * (result - winning_expectancy(self_rate, opponent_rate) + (3100 - self_rate) / 50000)


def calculate_player_rating(player_rating, opponents_data):
    
    """Вычисляем рейтинг игрока после нескольких туров"""
    round_count = len(opponents_data)
    next_rating = player_rating
    rate_growth = 0
    for rnd in opponents_data:
        if rnd[1] is None:
            round_count -= 1
            continue

        round_growth = round(growth(next_rating, rnd[0], rnd[1]))
        rate_growth += round_growth
        next_rating += round_growth
        # print('Прирост за', rnd[0], ':', round_growth)

    if rate_growth > abnormal_growth(player_rating, round_count):
        # print('Промежуточный рейтинг:', round(player_rating + rate_growth, 2))
        return calculate_player_rating(next_rating, opponents_data)

    return next_rating


def new_rating(self_rate, opponent_rate, result=1):
    return round(self_rate + growth(self_rate, opponent_rate, result), 2)
