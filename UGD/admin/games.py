from django.contrib.admin import ModelAdmin, site
from ..models.games import TournamentPlayer, Pairing


class TournamentPlayerAdmin(ModelAdmin):
    list_display = (
        'player',
        'tournament',
        'rank',
        'rating_start',
        'rating_finish'
    )
    fieldsets = (
        (None, {
            'fields': ('player', 'tournament', 'rank', 'place')
        }),
        ('Інформація про гравця', {
            'classes': ('wide',),
            'fields': ('rating_start', 'rating_finish', 'egd_rating_start', 'egd_rating_finish')
        })
    )
    search_fields = [
        'player',
        'tournament'
    ]


class PairingAdmin(ModelAdmin):
    list_display = (
        'player_black',
        'player_white',
        'tournament_round',
        'winner_color',
        'technical_win'
    )
    fieldsets = (
        (None, {
            'fields': ('player_black', 'player_white', 'tournament_round', 'color', 'handicap')
        }),
        ('Інформація про партію', {
            'classes': ('wide',),
            'fields': ('winner_color', 'technical_win', 'round_skip', 'game_record')
        })
    )
    search_fields = [
        'player_black',
        'player_white'
    ]

site.register(TournamentPlayer, TournamentPlayerAdmin)
site.register(Pairing, PairingAdmin)
