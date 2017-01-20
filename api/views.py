from django.http import HttpResponse, JsonResponse
from .parsers import egd_tables

# Create your views here.


def upload(request):
    if not request.GET:
        return JsonResponse(status=200, data={"status": "Empty GET-request"})
    if request.GET['type'] == 'egd_tables':
        data = egd_tables.upload_tournament(request)
        return JsonResponse(status=200, data=data, safe=False)


def download(request):
    return HttpResponse("Nothing here, sir...")
