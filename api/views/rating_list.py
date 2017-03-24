import re

from django.http import HttpResponse, JsonResponse

from UGD.models import Country, City, Player, Rank, LocalRank
from functions_data.current_rank import get_current_rank


def upload_active_rating_list(request):
    """
    Импортирует рейтинг-лист активных игроков
    :param request: в теле запроса должен находиться csv с информацией:
                    место, фамилия, имя, город, рейтинг, ранг, разряд
    :return: взвращается JSON с количеством успешных загрузок
    """
    count_created, count_updated = 0, 0
    file = request.body.decode().split(sep="\n")
    rating_list = []
    if file == ['[object FileList]']:
        return HttpResponse("Your request have no files or your file is empty.")
    for row in file:
        string = row.split(sep=";")
        if len(string) != 7:
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
            rank = get_current_rank(row[4])

        local_rank = re.match(r"(?P<local_rank>[МСУК123спрюн. ]+)+", row[6])

        try:
            local_rank = LocalRank.objects.get(abbreviate=local_rank.group('local_rank'))
        except (LocalRank.DoesNotExist, AttributeError):
            local_rank = None

        player = Player.objects.update_or_create(
            last_name=row[1],
            first_name=row[2],
            defaults={
                "city": city,
                "rating": row[4],
                "rank": rank,
                "local_rank": local_rank,
                "active": True
            }
        )
        if player[1]:
            count_created += 1
        else:
            count_updated += 1
        print(player)
    return JsonResponse(status=200, data={"Type": "Active players", "Updated": count_updated, "Created": count_created})


def upload_inactive_rating_list(request):
    """
    Импортирует рейтинг-лист неактивных игроков
    :param request: в теле запроса должен находиться csv с информацией:
                    фамилия, имя, город, рейтинг
    :return: взвращается JSON с количеством успешных загрузок
    """
    count_created, count_updated = 0, 0
    file = request.body.decode().split(sep="\n")
    rating_list = []
    if file == ['[object FileList]']:
        return HttpResponse("Your request have no files or your file is empty.")
    for row in file:
        string = row.split(sep=";")
        if len(string) != 5:
            continue
        rating_list.append(string)
    for row in rating_list:
        if row[3]:
            city = City.objects.get_or_create(
                name=row[3],
                defaults={
                    "country": Country.objects.get(id=1)
                }
            )[0]
        else:
            city = None

        player = Player.objects.update_or_create(
            last_name=row[1],
            first_name=row[2],
            defaults={
                "city": city,
                "rating": row[4],
                "rank": get_current_rank(int(row[4])),
                "active": False
            }
        )
        if player[1]:
            count_created += 1
        else:
            count_updated += 1
        print(player)
    return JsonResponse(status=200,
                        data={"Type": "Inactive players", "Updated": count_updated, "Created": count_created})


def download_rating_list(request):
    """
    Возвращает JSON рейтинг-листа активных игроков
    :return: json
    """
    data = {}
    for player in Player.objects.filter(active=True):
        if player.local_rank:
            local_rank = player.local_rank.abbreviate
        else:
            local_rank = ""
        if player.rank:
            rank = player.rank.name
        else:
            rank = ""
        if player.city is None:
            city = ""
        else:
            city = player.city.name
        data[player.id] = {
            "last_name": player.last_name,
            "first_name": player.first_name,
            "city": city,
            "rating": player.rating,
            "rank": rank,
            "local_rank": local_rank
        }
    return JsonResponse(status=200, data=data)
