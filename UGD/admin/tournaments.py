from django.contrib.admin import TabularInline, ModelAdmin, site
from ..models import Tournament, TournamentPlayer


class PlayerTournamentInline(TabularInline):
    model = TournamentPlayer
    extra = 0
    fields = ('place', 'player', 'rating_start', 'rating_finish')
    ordering = ['place']


class TournamentAdmin(ModelAdmin):
    inlines = [PlayerTournamentInline]
    list_display = (
        'name',
        'date_begin',
        'date_end',
        'city',
        'ranked',
        'egd_code',
        'table'
    )
    fieldsets = (
        (None, {
            'fields': ('name', 'date_begin', 'date_end', 'city')
        }),
        ('Інформація про турнір', {
            'classes': ('wide',),
            'fields': ('ranked', 'egd_code', 'table')
        })
    )
    search_fields = ['name']
    ordering = ['-date_begin', '-date_end']


site.register(Tournament, TournamentAdmin)
