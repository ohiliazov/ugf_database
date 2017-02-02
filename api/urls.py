from django.conf.urls import url
from .views import rating_list
# Create your urls here.

app_name = 'api'
urlpatterns = [
    url(r'^upload/active_rating_list/$', rating_list.upload_active_rating_list, name='upload_active_rating_list'),
    url(r'^upload/inactive_rating_list/$', rating_list.upload_inactive_rating_list, name='upload_inactive_rating_list'),
    url(r'^download/rating_list/$', rating_list.download_rating_list, name='download_rating_list'),
]
