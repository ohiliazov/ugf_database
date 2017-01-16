from django.conf.urls import url

from . import views

# Create your urls here.

app_name = 'UGD'
urlpatterns = [
    # Index
    url(r'^rating_list/$', views.RatingListView.as_view(), name='rating_list'),
    # Player info
    # url(r'^player/(?P<pk>[0-9]+)/$', views.PlayerInfoView.as_view(), name='player_info'),
]
