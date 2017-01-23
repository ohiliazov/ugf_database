from django.conf.urls import url
from .views import rating_list
# Create your urls here.

app_name = 'api'
urlpatterns = [
    url(r'^upload/rating_list/$', rating_list.upload_rating_list, name='upload_rating_list'),
    url(r'^download/rating_list/$', rating_list.download_rating_list, name='download_rating_list'),
]
