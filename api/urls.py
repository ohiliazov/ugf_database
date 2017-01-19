from django.conf.urls import url

from . import views

# Create your urls here.

app_name = 'players'
urlpatterns = [
    url(r'^players/ufgo/$', views.ufgo_players_upload, name='ufgo_players_upload'),
    url(r'^tournament_list/$', views.tournament_list_upload, name='tournament_list_upload'),
    url(r'^tournaments_upload/$', views.tournaments_upload, name='tournaments_upload'),
    url(r'^players/egd/$', views.egd_players_upload, name='egd_players_upload'),
    url(r'^upload_tournament/$', views.upload_tournament, name='upload_tournament'),
]
