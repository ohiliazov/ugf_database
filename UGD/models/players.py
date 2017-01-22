from django.db import models
from .clubs import City
from .ranks import Rank, LocalRank


class Player(models.Model):
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="прізвище"
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="ім'я"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="клуб"
    )
    rating = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="рейтинг УФГО"
    )
    rank = models.ForeignKey(
        Rank,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="ранг"
    )
    local_rank = models.ForeignKey(
        LocalRank,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="спортивний розряд"
    )
    sex = models.NullBooleanField(
        default=None,
        choices=(
            (False, '♀'),
            (True, '♂'),
        ),
        verbose_name="стать"
    )
    ufgo_member = models.BooleanField(
        default=False,
        verbose_name="Член УФГО"
    )
    egd_last_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="прізвище у EGD"
    )
    egd_first_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="ім'я у EGD"
    )
    egd_rating = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Єврорейтинг"
    )
    egd_place = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Місце у EGD"
    )
    egd_pin = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        verbose_name="Код гравця у EGD"
    )

    class Meta:
        verbose_name = "гравець"
        verbose_name_plural = "гравці"

    def __str__(self):
        if self.last_name and self.first_name:
            return self.last_name + ' ' + self.first_name
        elif self.egd_last_name and self.egd_first_name:
            return self.egd_last_name + ' ' + self.egd_first_name
        else:
            return self.id
