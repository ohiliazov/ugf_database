from UGD.models import TournamentPlayer, Pairing
from django.shortcuts import redirect
from functions.rate_calc_func import calculate_tournament_results


def tournament_rating_calculator(request, pk):

    player_list = TournamentPlayer.objects.filter(tournament__id=pk).order_by('place')
    start_ratings = {}
    tournament_data = {}
    for player in player_list:
        start_ratings[player.place] = float(player.rating_start)
        tournament_data[player.place] = list()
        pairing_list = Pairing.objects.filter(tournament_player=player)
        for pairing in pairing_list:
            opponent = pairing.tournament_player_opponent.place
            if pairing.round_skip or pairing.technical_result:
                result = None
            elif pairing.game_result:
                result = 1
            else:
                result = 0
            tournament_data[player.place].append((opponent, result))
    finish_ratings = calculate_tournament_results(6, start_ratings, tournament_data)
    for row in finish_ratings:
        print(row, finish_ratings[row])
    
    return redirect("UGD:tournament_info", pk=pk)
