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

    class Meta:
        fields = (
            'city',
            'ufgo_member'
        )
        row_attrs = {
            "onkeyup": 'myFunction(1)'
        }
