from django.contrib.admin import TabularInline, ModelAdmin, site
from ..models.clubs import Country, Club, City
from ..models.players import Player
from ..models.tournaments import Tournament


class ClubInline(TabularInline):
    model = Club
    extra = 0
    fields = ('name', 'egd_name')
    ordering = ['name']


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
        'egd_name',
        'egd_code'
    )
    extra = 0
    ordering = ['-date_begin', '-date_end']


class CountryAdmin(ModelAdmin):
    inlines = [ClubInline, CityInline]
    list_display = ('name', 'egd_name')
    search_fields = ['name', 'egd_name']
    ordering = ['name']


class CityAdmin(ModelAdmin):
    inlines = [TournamentInline]
    list_display = ('name', 'egd_name', 'country')
    search_fields = ['name', 'egd_name']
    ordering = ['country', 'name']


class ClubAdmin(ModelAdmin):
    inlines = [PlayerInline]
    list_display = ('name', 'egd_name', 'country')
    search_fields = ['name', 'egd_name']
    ordering = ['country', 'name']


site.register(Country, CountryAdmin)
site.register(City, CityAdmin)
site.register(Club, ClubAdmin)
