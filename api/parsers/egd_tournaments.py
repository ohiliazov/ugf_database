from UGD.models.tournaments import Tournament
from UGD.models.players import Player
from UGD.models.games import TournamentPlayer
from UGD.models.ranks import Rank

def get_tournament_list(request):
    file = open('/all.hst')
    for line in file:
        if len(line.split()) == 11:
            if line.split()[6] in [tournament.egd_code for tournament in Tournament.objects.all()]:
                if line.split()[0] in [player.egd_pin for player in Player.objects.all()]:
                    tournament = Tournament.objects.get(egd_code=line.split()[6])
                    player = Player.objects.get(egd_pin=line.split()[0])
                    if Rank.objects.get(egd_grade=line.split()[5]):
                        rank = Rank.objects.get(egd_grade=line.split()[5])
                    else:
                        rank = None
                    TournamentPlayer.objects.update_or_create(
                        player=player,
                        tournament=tournament,
                        defaults={
                            'rank': rank,
                            'egd_rating_start': line.split()[9],
                            'egd_rating_finish': line.split()[10]
                        }
                    )
                    print(str(player.__str__())+' @ '+str(tournament.__str__())+' - '+str(line.split()[9])+' --> '+str(line.split()[10]))
    file.close()