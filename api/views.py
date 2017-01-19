from django.http import HttpResponse
from .parsers import egd_players, ufgo_players, egd_tournaments, egd_table

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


def tournament_list_upload(request):
    if request.body:
        egd_tournaments.get_tournament_list(request)
        return HttpResponse("Загружено")
    return HttpResponse("No files")


def tournaments_upload(request):
    if request.body:
        egd_tournaments.tournaments_upload(request)
        return HttpResponse("Загружено")
    return HttpResponse("No files")


def upload_tournament(request):
    if request.GET['egd_code']:
        egd_table.tournament_info(request)
        return HttpResponse("Загружено")
    return HttpResponse("No files")
