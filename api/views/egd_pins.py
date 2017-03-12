from django.http import HttpResponse, JsonResponse
from UGD.models import Player
from functions import translit
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
    for translation in translit.ALL_TRANSLITERATIONS:
        for player in Player.objects.all():
            for row in pin_list:
                if row[1] == translit.translit(player.last_name, translation) \
                        and row[2] == translit.translit(player.first_name, translation) \
                        and not player.egd_pin:
                    player.egd_pin = row[0]
                    player.save()
                    print(translation, player, player.egd_pin)
                    count += 1
    return HttpResponse("%d rows updated" % count)
