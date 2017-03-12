from django.db import models

"""
This file contains next models:
    Country
    City
    Rank
    LocalRank
"""


class Country(models.Model):
    class Meta:
        verbose_name = "країна"
        verbose_name_plural = "країни"

    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="назва країни"
    )
    egd_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="країна в EGD"
    )

    def __str__(self):
        if self.name:
            return self.name
        elif self.egd_name:
            return self.egd_name
        else:
            return "Country %d" % self.id


class City(models.Model):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="назва міста"
    )
    egd_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="місто в EGD"
    )
    country = models.ForeignKey(
        Country,
        default=1,
        on_delete=models.CASCADE,
        verbose_name="країна"
    )

    class Meta:
        verbose_name = "місто"
        verbose_name_plural = "міста"

    def __str__(self):
        if self.name:
            return self.name
        elif self.egd_name:
            return self.egd_name
        else:
            return "City %d" % self.id


class Rank(models.Model):
    name = models.CharField(
        max_length=6,
        verbose_name="ранг"
    )
    demotion = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="нижня межа"
    )
    promotion = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="верхня межа"
    )
    egd_grade = models.CharField(
        null=True,
        blank=True,
        max_length=3,
        verbose_name="ранг у EGD"
    )

    class Meta:
        verbose_name = 'ранг'
        verbose_name_plural = 'ранги'

    def __str__(self):
        if self.name:
            return self.name
        elif self.egd_grade:
            return self.egd_grade
        else:
            return self.id


class LocalRank(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="спортивний розряд"
    )
    abbreviate = models.CharField(
        max_length=20,
        verbose_name="абревіатура"
    )

    class Meta:
        verbose_name = 'спортивний розряд'
        verbose_name_plural = "спортивні розряди"

    def __str__(self):
        if self.name:
            return self.name
        elif self.abbreviate:
            return self.abbreviate
        else:
            return self.id
