from django.db import models
from .tournaments import Tournament
from .players import Player
from .ranks import Rank


class TournamentPlayer(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        verbose_name="гравець"
    )
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        verbose_name="турнір"
    )
    rank = models.ForeignKey(
        Rank,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="ранг"
    )
    place = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="місце"
    )
    rating_start = models.DecimalField(
        null=True,
        blank=True,
        max_digits=8,
        decimal_places=4,
        verbose_name="рейтинг-1"
    )
    rating_finish = models.DecimalField(
        null=True,
        blank=True,
        max_digits=8,
        decimal_places=4,
        verbose_name="рейтинг-2"
    )
    egd_rating_start = models.DecimalField(
        null=True,
        blank=True,
        max_digits=8,
        decimal_places=4,
        verbose_name="рейтинг EGD-1"
    )
    egd_rating_finish = models.DecimalField(
        null=True,
        blank=True,
        max_digits=8,
        decimal_places=4,
        verbose_name="рейтинг EGD-2"
    )

    def __str__(self):
        if self.player.first_name and self.player.last_name:
            full_name = self.player.first_name+' '+self.player.last_name
        elif self.player.egd_first_name and self.player.egd_last_name:
            full_name = self.player.egd_first_name+' '+self.player.egd_last_name
        else:
            full_name = self.player.id
        if self.tournament.name:
            tournament_name = self.tournament.name
        elif self.tournament.egd_name:
            tournament_name = self.tournament.egd_name
        else:
            tournament_name = self.tournament.id
        return tournament_name+' @ '+full_name

    def get_rating_delta(self):
        if self.rating_start and self.rating_finish:
            return self.rating_finish - self.rating_start
        else:
            return "-"
    get_rating_delta.short_description = 'Δ Rating'


class Pairing(models.Model):
    HANDICAP_CHOICES = (
        (0, 'Без фори'),
        (1, 'Комі 0.5 очок'),
        (2, '2 камня'),
        (3, '3 камня'),
        (4, '4 камня'),
        (5, '5 каменів'),
        (6, '6 каменів'),
        (7, '7 каменів'),
        (8, '8 каменів'),
        (9, '9 каменів'),
    )
    player_black = models.ForeignKey(
        TournamentPlayer,
        null=True,
        verbose_name="чорні",
        related_name="player_black"
    )
    player_white = models.ForeignKey(
        TournamentPlayer,
        null=True,
        verbose_name="білі",
        related_name="player_white"
    )
    tournament_round = models.PositiveIntegerField(
        verbose_name="раунд"
    )
    color = models.BooleanField(
        default=False,
        verbose_name="колір"
    )
    handicap = models.PositiveIntegerField(
        default=0,
        choices=HANDICAP_CHOICES,
        verbose_name="гандікап"
    )
    winner_color = models.NullBooleanField(
        default=None,
        verbose_name="колір переможця"
    )
    technical_win = models.BooleanField(
        default=False,
        verbose_name="технічна перемога"
    )
    round_skip = models.BooleanField(
        default=False,
        verbose_name="Пропуск туру"
    )
    game_record = models.FileField(
        null=True,
        blank=True,
        upload_to='uploads/game_records/'
    )

    def __str__(self):
        return self.player_black.tournament+' @ '+self.player_black.player+' vs. '+self.player_white.player
