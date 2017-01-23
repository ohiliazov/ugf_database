from UGD.models.ranks import Rank, LocalRank
from UGD.models.players import Player
from UGD.models.clubs import City


def upload_rating_list(request):
    count = 0
    file = request.body.decode().split(sep="\n")
    table_data = []
    for line in file:
        string = line.split(sep=";")
        table_data.append(string)
    for line in table_data:
        city = City.objects.get_or_create(
            country__id=1,
            name=line[2]
        )
        rank = Rank.objects.get(name=line[4])
        try:
            local_rank = LocalRank.objects.get(abbreviate=line[5])
        except LocalRank.DoesNotExist:
            local_rank = None
        if line[6]:
            ufgo_member = True
        else:
            ufgo_member = False
        player = Player.objects.get_or_create(
            last_name=line[0],
            first_name=line[1],
            defaults={
                'rating': line[3],
                'rank': rank,
                'local_rank': local_rank,
                'city': city[0],
                'ufgo_member': ufgo_member
            }
        )
        print(player+' - OK')
        count += 1
    return count
