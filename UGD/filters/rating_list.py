import django_filters
from ..models.players import Player
from ..models.clubs import Club


class PlayersFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(
        lookup_expr='contains',
        label="Прізвище"
    )
    first_name = django_filters.CharFilter(
        lookup_expr='contains',
        label="Ім'я"
    )
    city = django_filters.ChoiceFilter(
        choices=[(city.id, city.name) for city in Club.objects.all()],
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
        model = Player
        fields = (
            'last_name',
            'first_name'
        )
