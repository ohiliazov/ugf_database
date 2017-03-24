from django.conf.urls import url

from .views import *

# Create your urls here.

app_name = 'json_ugd'
urlpatterns = [
    url(r'^rating_list/$', json_rating_list, name='json_rating_list'),
]
