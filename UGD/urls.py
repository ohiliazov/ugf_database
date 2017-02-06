from django.conf.urls import url
from .views import rating_list, tournament_list, player_info, tournament_info, links, rating_calculator

# Create your urls here.

app_name = 'UGD'
urlpatterns = [
    # Rating list
    url(r'^rating_list/$', rating_list.RatingListView.as_view(), name='rating_list'),
    url(r'^tournament_list/$', tournament_list.TournamentListView.as_view(), name='tournament_list'),

    # EGD links
    url(r'^egd_player/(?P<egd_pin>[\d]+)/$', links.egd_player_link, name='egd_player_link'),
    url(r'^egd_tournament/(?P<egd_code>[\d\w]+)/$', links.egd_tournament_link, name='egd_tournament_link'),

    #
    url(r'^rating_calculator/$', rating_calculator.RatingCalculatorView.as_view(), name='rating_calculator'),

    # Player info
    url(r'^player/(?P<pk>[0-9]+)/$', player_info.PlayerInfoView.as_view(), name='player_info'),
    url(r'^tournament/(?P<pk>[0-9]+)/$', tournament_info.TournamentInfoView.as_view(), name='tournament_info'),
]
