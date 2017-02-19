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


def growth(self_rate, opponent_rate, result=1):
    return con(self_rate) * (result - winning_expectancy(self_rate, opponent_rate) + (3100 - self_rate) / 50000)


def new_rating(self_rate, opponent_rate, result=1):
    return self_rate + growth(self_rate, opponent_rate, result)
