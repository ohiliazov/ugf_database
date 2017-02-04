from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


def egd_link(request, egd_pin):
    return redirect("http://www.europeangodatabase.eu/EGD/Player_Card.php?key="+egd_pin)
