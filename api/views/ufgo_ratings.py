import re
from django.http import HttpResponse

INFO_TAGS = [
    'TC'
]


def upload_ufgo_ratings(request):
    file = request.body.decode().split(sep="\n")
    tournament_code = ''
    for line in file:
        print(line)
        tag = re.match(r"^; TC\[(?P<value>[\w\W]+)+\]+", line)
        tournament_code = tag.group('value')
    print(tournament_code)
    return HttpResponse("Good.")
