from functions.translit import translit, UkrainianKMU
from UGD.models.ranks import Rank, LocalRank
from UGD.models.players import Player
from UGD.models.clubs import Club


def parse(request):
    count = 0
    file = request.body.decode().split(sep="\n")
    table_data = []
    for line in file:
        string = line.split(sep=";")
        table_data.append(string)
    for line in table_data:
        city = Club.objects.get_or_create(
            country__id=1,
            name=line[2]
        )
        rank = Rank.objects.get(name=line[4])
        local_rank = LocalRank.objects.get(abbreviate=line[5])
        try:
            player = Player.objects.get(
                last_name=line[0],
                first_name=line[1]
            )
        except Player.DoesNotExist:
            print(line[0]+' '+line[1]+' - ERROR 1 (DoesNotExist)')
        else:
            player.last_name = line[0]
            player.first_name = line[1]
            player.rating = line[3]
            player.rank = rank
            player.local_rank = local_rank
            player.city = city[0]
            if line[6]:
                player.ufgo_member = True
            player.save()
            print(line[0]+' '+line[1]+' - OK')
        count += 1
    return count

