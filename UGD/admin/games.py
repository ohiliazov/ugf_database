from django.contrib.admin import ModelAdmin, site
from ..models.games import TournamentPlayer


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

site.register(TournamentPlayer, TournamentPlayerAdmin)
