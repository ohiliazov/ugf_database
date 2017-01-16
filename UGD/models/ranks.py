from django.db import models


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
