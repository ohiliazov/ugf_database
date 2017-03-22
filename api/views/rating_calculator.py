from UGD.models import TournamentPlayer, Pairing, Player
from django.shortcuts import redirect
from functions.rate_calc_func import calculate_tournament


def tournament_rating_calculator(request, pk):

    player_list = TournamentPlayer.objects.filter(tournament__id=pk).order_by('place')
    start_ratings = {}
    tournament_data = {}
    for player in player_list:
        start_ratings[player.place] = float(player.rating_start)
        tournament_data[player.place] = list()
        pairing_list = Pairing.objects.filter(pairing_player=player)
        for pairing in pairing_list:
            opponent = pairing.pairing_opponent.place
            if pairing.round_skip or pairing.technical_result:
                result = None
            elif pairing.game_result:
                result = 1
            else:
                result = 0
            tournament_data[player.place].append((opponent, result))
    print(start_ratings)
    print(tournament_data)
    finish_ratings = calculate_tournament(start_ratings, tournament_data)
    for row in finish_ratings:
        player = player_list.get(place=row)
        player.rating_finish = finish_ratings[row]
        player.save()
        print(row, start_ratings[row], finish_ratings[row])

    return redirect("UGD:tournament_info", pk=pk)


def update_rating_list(request):
    all_active_players = Player.objects.filter(active=True)
    for player in all_active_players:
        tourney = TournamentPlayer.objects.filter(player=player, tournament__date_begin__year__gte=2017).order_by('-tournament__date_begin').first()
        if tourney is not None:
            player.rating = tourney.rating_finish
            player.save()
            print(player, player.rating)

    return redirect("UGD:rating_list")
