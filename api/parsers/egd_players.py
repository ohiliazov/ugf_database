from UGD.models.clubs import Country, Club
from UGD.models.players import Player


def parse(request):
    count = 0
    file = request.body.decode().split(sep="\n")
    table_data = []
    for line in file:
        string = line.split(sep=";")
        table_data.append(string)
        print(string)
    for line in table_data:
        country = Country.objects.get_or_create(egd_name=line[3])
        club = Club.objects.get_or_create(
            country=country[0],
            egd_name=line[4]
        )
        player = Player.objects.update_or_create(
            egd_pin=line[0],
            defaults={
                'egd_last_name': line[1],
                'egd_first_name': line[2],
                'club': club[0],
                'egd_rating': line[5],
                'egd_place': line[7]
            }
        )
        print(player)
        count += 1
    return count
