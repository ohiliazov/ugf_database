from django.contrib.admin import ModelAdmin, site
from ..models.tournaments import Tournament


class TournamentAdmin(ModelAdmin):
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
