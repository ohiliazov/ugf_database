from UGD.models.tournaments import Tournament
from UGD.models.players import Player
from UGD.models.games import TournamentPlayer
from UGD.models.ranks import Rank
from UGD.models.clubs import Country, City
import datetime
import re


def get_tournament_list(request):
    file = open('D:/Python/ugf_database/api/parsers/all2.hst')
    for line in file:
        if len(line.split()) == 11:
            if line.split()[6] in [tournament.egd_code for tournament in Tournament.objects.all()]:
                if line.split()[0] in [player.egd_pin for player in Player.objects.all()]:
                    tournament = Tournament.objects.get(egd_code=line.split()[6])
                    player = Player.objects.get(egd_pin=line.split()[0])
                    if Rank.objects.get(egd_grade=line.split()[5]):
                        rank = Rank.objects.get(egd_grade=line.split()[5])
                    else:
                        rank = None
                    TournamentPlayer.objects.update_or_create(
                        player=player,
                        tournament=tournament,
                        defaults={
                            'rank': rank,
                            'egd_rating_start': line.split()[9],
                            'egd_rating_finish': line.split()[10]
                        }
                    )
                    print(str(player.__str__())+' @ '+str(tournament.__str__())+' - '+str(line.split()[9])+' --> '+str(line.split()[10]))
    file.close()


def tournaments_upload(request):
    file = open('D:/Python/ugf_database/api/parsers/tourn.txt')
    for line in file:
        if len(line.split(maxsplit=6)) == 7 and line.split(maxsplit=6)[0] in [tournament.egd_code for tournament in Tournament.objects.all()]:
            tournament = Tournament.objects.get(egd_code=line.split(maxsplit=6)[0])
            reg_date = re.match(r".(?P<date>[\d]+)+", line.split(maxsplit=6)[0])
            tournament.date_begin = datetime.datetime.strptime(reg_date.group('date'), "%y%m%d").date()
            print(tournament.date_begin)
            if tournament.date_begin.weekday() == 0:
                temp_weekday = 7
            else:
                temp_weekday = tournament.date_begin.weekday()
            tournament.date_end = tournament.date_begin + datetime.timedelta(6 - temp_weekday)
            print(tournament.date_end)
            reg_country = re.match(r"\((?P<country>[\w]+)+\)", line.split(maxsplit=6)[4])
            reg_city = re.match(r"(?P<city>[\w\s-]+)+", line.split(maxsplit=6)[5])
            country = Country.objects.update_or_create(egd_name=reg_country.group('country'))
            city = City.objects.update_or_create(country=country[0], egd_name=reg_city.group('city'))
            print(city[0], country[0])
            tournament.city = city[0]
            tournament.egd_class = line.split(maxsplit=6)[1]
            tournament.egd_name = line.split(maxsplit=6)[6]
            tournament.save()
            # print(line.split(maxsplit=6))
            # print(tournament)
    file.close()
