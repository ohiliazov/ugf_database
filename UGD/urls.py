from django.conf.urls import url

from .views import rating_list

# Create your urls here.

app_name = 'UGD'
urlpatterns = [
    # Index
    url(r'^rating_list/$', rating_list.RatingListView.as_view(), name='rating_list'),
    # Player info
    # url(r'^player/(?P<pk>[0-9]+)/$', rating_list.PlayerInfoView.as_view(), name='player_info'),
]
