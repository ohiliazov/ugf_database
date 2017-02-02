import django_filters
from ..models.players import Player
from ..models.clubs import City


class PlayersFilter(django_filters.FilterSet):
    city = django_filters.ChoiceFilter(
        choices=[(city.id, city.name) for city in City.objects.all()],
        empty_label="--Не обрано--",
        label="Місто"
    )
    ufgo_member = django_filters.ChoiceFilter(
        choices=[
            (False, 'Ні'),
            (True, 'Так')
        ],
        name="ufgo_member",
        label="Член УФГО",
    )
    active = django_filters.ChoiceFilter(
        choices=[
            (False, 'Ні'),
            (True, 'Так')
        ],
        name="active",
        label="Активні гравці",
    )

    class Meta:
        model = Player
        fields = (
            'city',
            'ufgo_member',
            'active'
        )
