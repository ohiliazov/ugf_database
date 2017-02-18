from django.db import models
from . import City


class Tournament(models.Model):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="назва турніру"
    )
    date_begin = models.DateField(
        null=True,
        blank=True,
        verbose_name="дата початку"
    )
    date_end = models.DateField(
        null=True,
        blank=True,
        verbose_name="дата завершення"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="місто"
    )
    ranked = models.NullBooleanField(
        default=True,
        choices=(
            (False, 'Ні'),
            (True, 'Так'),
        ),
        max_length=1,
        verbose_name="рейтинговий"
    )
    egd_code = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        verbose_name="код турніру в EGD"
    )
    table = models.FileField(
        null=True,
        blank=True,
        upload_to='uploads/tournaments/',
        verbose_name="турнірна таблиця"
    )

    class Meta:
        verbose_name = "турнір"
        verbose_name_plural = "турніри"

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.id)

    def get_number_of_players(self):
        return self.tournamentplayer_set.count()

    def get_number_of_games(self):
        return (self.tournamentplayer_set.filter(pairing_player__isnull=False).count() - 2 *
                self.tournamentplayer_set.filter(pairing_opponent__isnull=True).count()) // 2
