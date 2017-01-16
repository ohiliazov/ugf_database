from UGD.models.tournaments import Tournament
from UGD.models.players import Player


def get_tournament_list(request):
    file = open('/all.hst')
    count = 0
    tournament_list = set()
    for line in file:
        if len(line.split()) == 11 and line.split()[3] == 'UA' and line.split()[0] in [player.egd_pin for player in Player.objects.all()]:
            # print(line.split())
            tournament_list.add(line.split()[6])
            print(line.split()[6])
            Tournament.objects.update_or_create(egd_name=line.split()[6])
            # count += 1
        # if count > 5:
        #     file.close()
        #     break
        count += 1
        print(count)
    file.close()
    print([line for line in tournament_list])
    print(Tournament.objects.all())