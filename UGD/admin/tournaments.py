from django.contrib.admin import ModelAdmin, site
from ..models.tournaments import Tournament


class TournamentAdmin(ModelAdmin):
    list_display = (
        'name',
        'date_begin',
        'date_end',
        'city',
        'ranked',
		'egd_name',
		'egd_class',
        'egd_code',
        'table'
    )
    fieldsets = (
        (None, {
            'fields': ('name', 'date_begin', 'date_end', 'city')
        }),
        ('Інформація про турнір', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('ranked', 'egd_name', 'egd_class', 'egd_code', 'table')
        })
    )
    search_fields = ['name', 'egd_name']
    ordering = ['-date_begin', '-date_end']


site.register(Tournament, TournamentAdmin)
