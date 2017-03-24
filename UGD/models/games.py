from decimal import Decimal

from django.db import models

from . import City, Rank, LocalRank

"""
В этом файле содержится информация об игроках, турнирах и результатах партий.
"""


class Player(models.Model):
    class Meta:
        verbose_name = "гравець"
        verbose_name_plural = "гравці"

    last_name = models.CharField(null=True, blank=True, max_length=255, verbose_name="прізвище")
    first_name = models.CharField(null=True, blank=True, max_length=255, verbose_name="ім'я")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="місто")

    place = models.PositiveIntegerField(null=True, blank=True, verbose_name="позиція в рейтингу")
    rating = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=4, verbose_name="рейтинг")

    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ранг")
    local_rank = models.ForeignKey(LocalRank, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="розряд")

    sex = models.NullBooleanField(default=None, choices=((False, '♀'), (True, '♂'),), verbose_name="стать")
    ufgo_member = models.BooleanField(default=False, verbose_name="Член УФГО")

    active = models.BooleanField(default=False, verbose_name="Активний")
    egd_pin = models.CharField(null=True, blank=True, max_length=8, verbose_name="Код гравця у EGD")

    def __str__(self):
        if self.last_name and self.first_name:
            return self.last_name + ' ' + self.first_name
        else:
            return "Player %d" % self.id

    def get_local_rank(self):
        """
        Returns rank of the player
        :return: string
        """
        if self.local_rank:
            return self.local_rank.abbreviate
        else:
            return ""

    def get_full_name(self):
        """
        Returns full name of the player
        :return: str
        """
        if self.last_name and self.first_name:
            return self.last_name + ' ' + self.first_name
        elif self.last_name:
            return self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return ""

    def get_city(self):
        """
        Returns city of the player
        :return: string
        """
        if self.city:
            return self.city.name
        else:
            return ""

    def get_rank(self):
        """
        Returns rank of the player
        :return: decimal
        """
        if self.rank:
            return self.rank.name
        else:
            return ""

    def get_rating(self):
        """
        Returns rating of the player
        :return: decimal
        """
        if self.rating:
            return round(self.rating)
        else:
            return ""

    def count_player_tournaments(self):
        """
        Returns number of attended tournaments
        :return: int
        """
        return self.tournamentplayer_set.count()

    def count_player_games(self):
        """
        Returns total number of played games
        :return: int
        """
        return self.tournamentplayer_set.filter(pairing_opponent__isnull=False).count()


class Tournament(models.Model):
    class Meta:
        verbose_name = "турнір"
        verbose_name_plural = "турніри"

    YES_NO_CHOICES = ((False, 'Ні'), (True, 'Так'),)

    name = models.CharField(null=True, blank=True, max_length=255, verbose_name="назва турніру")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="місто")

    date_begin = models.DateField(null=True, blank=True, verbose_name="дата початку")
    date_end = models.DateField(null=True, blank=True, verbose_name="дата завершення")

    ranked = models.NullBooleanField(default=True, choices=YES_NO_CHOICES, max_length=1, verbose_name="рейтинговий")
    egd_code = models.CharField(null=True, blank=True, max_length=8, verbose_name="код турніру в EGD")

    table = models.FileField(null=True, blank=True, upload_to='uploads/tournaments/', verbose_name="турнірна таблиця")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Tournament %d" % self.id

    def count_tournament_players(self):
        """
        Returns the number of participants
        :return: int
        """
        return self.tournamentplayer_set.count()

    def count_tournament_games(self):
        """
        Returns the number of actually played games. Skips games without opponent.
        :return: int
        """
        return (self.tournamentplayer_set.filter(pairing_player__isnull=False).count() - 2 *
                self.tournamentplayer_set.filter(pairing_opponent__isnull=True).count()) // 2


class TournamentPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name="гравець")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name="турнір")
    rank = models.ForeignKey(Rank, null=True, blank=True, on_delete=models.CASCADE, verbose_name="ранг")

    place = models.PositiveIntegerField(null=True, blank=True, verbose_name="місце")

    rating_start = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=4, verbose_name="R1")
    rating_finish = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=4, verbose_name="R2")

    class Meta:
        verbose_name = "учасник турніру"
        verbose_name_plural = "учасники турніру"

    def __str__(self):
        return "%s @ %s" % (self.tournament.name, self.player.get_full_name())

    def get_rating_delta(self):
        """
        Returns difference between ratings before and after the tournament
        :return: Decimal
        """
        if self.rating_start and self.rating_finish:
            return Decimal(self.rating_finish - self.rating_start).normalize()
        else:
            return ""

    def get_rating_start(self):
        """
        Returns normalized start rating
        :return: Decimal
        """
        if self.rating_start:
            return Decimal(self.rating_start).normalize()
        else:
            return ""

    def get_rating_finish(self):
        """
        Returns normalized finish rating
        :return: Decimal
        """
        if self.rating_finish:
            return Decimal(self.rating_finish).normalize()
        else:
            return ""

    def get_games_count(self):
        """
        Returns number of actually played games, i.e. with opponent
        :return: int
        """
        return self.pairing_player.filter(tournament_player_opponent__isnull=False).count()

    def get_wins_count(self):
        """
        Returns total number of wins
        :return: int
        """
        return self.pairing_player.filter(game_result=True).count()

    def get_result(self):
        """
        Returns the string like 4/5 (four wins of five games)
        :return:
        """
        return "%d/%d" % (self.get_wins_count(), self.get_games_count())


class Pairing(models.Model):
    class Meta:
        verbose_name = "результат партії"
        verbose_name_plural = "результати партії"

    COLOR_CHOICES = ((None, 'Невідомо'), ('b', 'Чорні'), ('w', 'Білі'))
    HANDICAP_CHOICES = (
        (0, 'Без фори'),
        (1, 'Комі 0.5 очок'), (2, '2 камня'), (3, '3 камня'),
        (4, '4 камня'), (5, '5 каменів'), (6, '6 каменів'),
        (7, '7 каменів'), (8, '8 каменів'), (9, '9 каменів')
    )

    pairing_player = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE,
        verbose_name="гравець", related_name="pairing_player")
    pairing_opponent = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE,
        default=None, null=True, blank=True, verbose_name="суперник", related_name="pairing_opponent")

    tournament_round = models.PositiveIntegerField(verbose_name="раунд")
    color = models.CharField(null=True, blank=True, max_length=1, choices=COLOR_CHOICES, verbose_name="колір")
    handicap = models.PositiveIntegerField(default=0, choices=HANDICAP_CHOICES, verbose_name="гандікап")

    game_result = models.NullBooleanField(verbose_name="перемога")
    technical_result = models.BooleanField(default=False, verbose_name="технічний результат")
    round_skip = models.BooleanField(default=False, verbose_name="Пропуск туру")

    game_record = models.FileField(null=True, blank=True, upload_to='uploads/game_records/')

    def __str__(self):
        if self.pairing_opponent:
            return str(self.pairing_player.tournament.name) + ' @ ' + \
                   str(self.pairing_player) + ' vs. ' + \
                   str(self.pairing_opponent.player)
        else:
            return str(self.pairing_player.tournament.name) + ' @ ' + \
                   str(self.pairing_player) + ' - пропуск туру'
