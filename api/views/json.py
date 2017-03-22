from django.db.models import Q
from django.http import JsonResponse

from UGD.models import Player
from functions import rate_calc_func


def json_player_list(request):
    """
    Player list
    :param request: GET should have full_name
    :return: JSON of matched players
    """
    try:
        players = Player.objects.filter(
            Q(active=True),
            Q(last_name__contains=request.GET['full_name']) |
            Q(first_name__contains=request.GET['full_name'])
        ).order_by('-rating')[:10]
    except KeyError:
        players = Player.objects.filter(active=True).order_by('-rating')
    data = {}
    for player in players:
        data[player.pk] = (player.get_full_name(), float(player.get_rating()))
    return JsonResponse(status=200, data=data)


def json_calculated_rating(request):
    """
    Rating calculator
    :param request: GET must have float ratings of players and result 1, 0.5 or 0 (or any float -_-)
    :return: JSON of rating calculations
    """
    try:
        first_rating = float(request.GET['first_rating'])
        second_rating = float(request.GET['second_rating'])
        result = float(request.GET['result'])
    except (KeyError, ValueError):
        return JsonResponse(status=400, data={"error_message": "Bad data"})
    else:
        data = {
            "first_player": {
                "next_rating": round(rate_calc_func.new_rating(first_rating, second_rating, result), 2),
                "alternative_rating": round(rate_calc_func.new_rating(first_rating, second_rating, (1 - result)), 2),
                "winning_expectancy": round(rate_calc_func.winning_expectancy(first_rating, second_rating), 2),
                "con_param": round(rate_calc_func.k_factor(first_rating), 2),
                "a_factor": round(rate_calc_func.a_factor(first_rating), 2)
            },
            "second_player": {
                "next_rating": round(rate_calc_func.new_rating(second_rating, first_rating, (1 - result)), 2),
                "alternative_rating": round(rate_calc_func.new_rating(second_rating, first_rating, result), 2),
                "winning_expectancy": round(rate_calc_func.winning_expectancy(second_rating, first_rating), 2),
                "con_param": round(rate_calc_func.k_factor(second_rating), 2),
                "a_factor": round(rate_calc_func.a_factor(second_rating), 2)
            }
        }
        return JsonResponse(status=200, data=data)


def json_rating_list(request):
    """
    Rating list
    :param request: GET should have full_name
    :return: JSON of matched players
    """
    try:
        players = Player.objects.filter(
            Q(active=True),
            Q(last_name__contains=request.GET['full_name']) |
            Q(first_name__contains=request.GET['full_name'])
        ).order_by('-rating')[:10]
    except KeyError:
        players = Player.objects.filter(active=True).order_by('-rating')
    data = {}
    for player in players:
        data[player.pk] = (player.get_full_name(), float(player.get_rating()))
    return JsonResponse(status=200, data=data)
