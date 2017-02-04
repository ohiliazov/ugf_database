from django.conf.urls import url
from .views import rating_list, player_info, links

# Create your urls here.

app_name = 'UGD'
urlpatterns = [
    # Index
    url(r'^rating_list/$', rating_list.RatingListView.as_view(), name='rating_list'),
    url(r'^egd_player/(?P<egd_pin>[0-9]+)/$', links.egd_link, name='egd_link'),
    # Player info
    url(r'^player/(?P<pk>[0-9]+)/$', player_info.PlayerInfoView.as_view(), name='player_info'),
]
