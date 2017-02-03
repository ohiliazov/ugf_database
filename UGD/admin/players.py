from django.contrib.admin import ModelAdmin, site
from ..models.players import Player


class PlayerAdmin(ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'city',
        'rating',
        'rank'
    )
    fieldsets = (
        (None, {
            'fields': ('last_name', 'first_name', 'city', 'sex')
        }),
        ('Інформація про гравця', {
            'classes': ('wide',),
            'fields': ('rating', 'rank', 'local_rank', 'ufgo_member')
        }),
        ('Гравець у EGD', {
            'classes': ('collapse',),
            'fields': ('egd_pin',)
        })
    )
    search_fields = [
        'last_name',
        'first_name'
    ]
    ordering = ['-rating']


site.register(Player, PlayerAdmin)
