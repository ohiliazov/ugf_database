from django.shortcuts import redirect


def egd_player_link(request, egd_pin):
    return redirect("http://www.europeangodatabase.eu/EGD/Player_Card.php?key=%s" % egd_pin)


def egd_tournament_link(request, egd_code):
    return redirect("http://europeangodatabase.eu/EGD/Tournament_Card.php?key=%s" % egd_code)

