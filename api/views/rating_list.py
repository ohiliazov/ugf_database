from django.http import HttpResponse, JsonResponse
from UGD.models.ranks import Rank, LocalRank
from UGD.models.players import Player
from UGD.models.clubs import City, Country
import re
# Create your views here.


def upload_rating_list(request):
    count_created, count_updated = 0, 0
    file = request.body.decode().split(sep="\n")
    rating_list = []
    if file == ['[object FileList]']:
        return HttpResponse("Your request have no files or your file is empty.")
    for row in file:
        string = row.split(sep=";")
        if len(string) != 8:
            continue
        rating_list.append(string)
    for row in rating_list:
        if row[3]:
            city = City.objects.get_or_create(
                country=Country.objects.get(id=1),
                name=row[3]
            )[0]
        else:
            city = None

        try:
            rank = Rank.objects.get(name=row[5])
        except Rank.DoesNotExist:
            rank = None

        try:
            local_rank = LocalRank.objects.get(abbreviate=row[6])
        except LocalRank.DoesNotExist:
            local_rank = None

        if re.match(r"(УФГО)", row[7]):
            ufgo_member = True
        else:
            ufgo_member = False

        player = Player.objects.update_or_create(
            last_name=row[1],
            first_name=row[2],
            defaults={
                "city": city,
                "rating": row[4],
                "rank": rank,
                "local_rank": local_rank,
                "ufgo_member": ufgo_member
            }
        )
        if player[1]:
            count_created += 1
        else:
            count_updated += 1
        print(player)
    return JsonResponse(status=200, data={"Updated": count_updated, "Created": count_created})


def download_rating_list(request):
    data = {}
    for player in Player.objects.filter():
        if player.local_rank:
            local_rank = player.local_rank.abbreviate
        else:
            local_rank = ""
        if player.rank:
            rank = player.rank.name
        else:
            rank = ""
        data[player.id] = {
            "last_name": player.last_name,
            "first_name": player.first_name,
            "city": player.city.name,
            "rating": player.rating,
            "rank": rank,
            "local_rank": local_rank
        }
    return JsonResponse(status=200, data=data)
