from django.contrib.admin import ModelAdmin, site
from ..models import Rank, LocalRank


class RankAdmin(ModelAdmin):
    list_display = ('name', 'egd_grade', 'demotion', 'promotion')
    search_fields = ['name', 'egd_grade']


class LocalRankAdmin(ModelAdmin):
    list_display = ('name', 'abbreviate')
    search_fields = ['name', 'abbreviate']


site.register(Rank, RankAdmin)
site.register(LocalRank, LocalRankAdmin)
