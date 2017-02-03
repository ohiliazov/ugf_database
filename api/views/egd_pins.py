from django.http import HttpResponse, JsonResponse
from UGD.models.players import Player
from functions.translit import translit
import re
# Create your views here.


def upload_egd_pins(request):
    count = 0
    file = request.body.decode().split(sep="\n")
    pin_list = []
    if file == ['[object FileList]']:
        return HttpResponse("Your request have no files or your file is empty.")
    for row in file:
        string = row.split(sep=";")
        if len(string) != 3:
            continue
        pin_list.append(string)
    print(pin_list)
    for player in Player.objects.all():
        for row in pin_list:
            if row[1] == translit(player.last_name) and row[2] == translit(player.first_name):
                player.egd_pin = row[0]
                print(player, player.egd_pin)
                count += 1
    return HttpResponse("%d rows updated" % count)
