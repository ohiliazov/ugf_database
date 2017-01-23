from django.http import HttpResponse, JsonResponse
from .parsers import egd_tables, ufgo_players
# Create your views here.


def upload(request):
    if not request.GET:
        return JsonResponse(status=200, data={"status": "Empty GET-request"})
    if request.GET['type'] == 'egd_tables':
        data = egd_tables.upload_tournament(request)
    elif request.GET['type'] == 'rating_list':
        print(1)
        if not request.body:
            print(2)
            return JsonResponse(status=200, data={"status": "Empty GET-request"})
        else:
            print(3)
            data = ufgo_players.upload_rating_list(request)
        return JsonResponse(status=200, data=data, safe=False)


def download(request):
    return HttpResponse("Nothing here, sir...")
