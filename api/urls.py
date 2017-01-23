from django.conf.urls import url

from . import views

# Create your urls here.

app_name = 'api'
urlpatterns = [
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^download/$', views.download, name='download'),
]
