from django.http import HttpResponse
from .parsers import egd_players, ufgo_players

# Create your views here.


def ufgo_players_upload(request):
    if request.body:
        ufgo_players.parse(request)
        return HttpResponse("Загружено")
    return HttpResponse("No files")


def egd_players_upload(request):
    if request.body:
        egd_players.parse(request)
        return HttpResponse("Загружено")
    return HttpResponse("No files")
