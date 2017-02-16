import django_filters
from ..models import Tournament
# todo Обновить фильтры для работы со скриптом


class TournamentsFilter(django_filters.FilterSet):
    class Meta:
        model = Tournament
        fields = (
            'date_begin',
            'date_end'
        )
