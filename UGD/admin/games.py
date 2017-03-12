from django.contrib.admin import ModelAdmin, site
from ..models import TournamentPlayer, Pairing


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
            'fields': ('rating_start', 'rating_finish')
        })
    )
    search_fields = [
        'player',
        'tournament'
    ]


class PairingAdmin(ModelAdmin):
    list_display = (
        'pairing_player',
        'pairing_opponent',
        'tournament_round',
        'game_result'
    )
    fieldsets = (
        (None, {
            'fields': ('pairing_player', 'pairing_opponent', 'tournament_round', 'color', 'handicap')
        }),
        ('Інформація про партію', {
            'classes': ('wide',),
            'fields': ('game_result', 'technical_result', 'round_skip', 'game_record')
        })
    )
    search_fields = [
        'pairing_player',
        'pairing_opponent'
    ]

site.register(TournamentPlayer, TournamentPlayerAdmin)
site.register(Pairing, PairingAdmin)
