from django.conf.urls import url

from . import views

# Create your urls here.

app_name = 'players'
urlpatterns = [
    url(r'^players/ufgo/$', views.ufgo_players_upload, name='ufgo_players_upload'),
    url(r'^players/egd/$', views.egd_players_upload, name='egd_players_upload'),
]
