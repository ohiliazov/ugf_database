from django.contrib.admin import TabularInline, ModelAdmin, site
from ..models import Country, City, Player, Tournament


class CityInline(TabularInline):
    model = City
    extra = 0
    fields = ('name', 'egd_name')
    ordering = ['name']


class PlayerInline(TabularInline):
    model = Player
    fields = (
        'last_name',
        'first_name',
        'rating',
        'rank',
        'local_rank',
        'egd_pin'
    )
    extra = 0
    ordering = ['-rating']


class TournamentInline(TabularInline):
    model = Tournament
    fields = (
        'name',
        'date_begin',
        'date_end',
        'city',
        'egd_code'
    )
    extra = 0
    ordering = ['-date_begin', '-date_end']


class CountryAdmin(ModelAdmin):
    inlines = [CityInline]
    list_display = ('name', 'egd_name')
    search_fields = ['name', 'egd_name']
    ordering = ['name']


class ClubAdmin(ModelAdmin):
    inlines = [PlayerInline]
    list_display = ('name', 'egd_name', 'country')
    search_fields = ['name', 'egd_name']
    ordering = ['country', 'name']


site.register(Country, CountryAdmin)
site.register(City, ClubAdmin)
