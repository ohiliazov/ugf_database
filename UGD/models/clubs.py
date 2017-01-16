from django.db import models


class Country(models.Model):
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

    class Meta:
        verbose_name = "країна"
        verbose_name_plural = "країни"

    def __str__(self):
        if self.name:
            return self.name
        elif self.egd_name:
            return self.egd_name
        else:
            return self.id


class Club(models.Model):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="назва клубу"
    )
    egd_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="клуб в EGD"
    )
    country = models.ForeignKey(
        Country,
        default=1,
        on_delete=models.CASCADE,
        verbose_name="країна"
    )

    class Meta:
        verbose_name = "клуб"
        verbose_name_plural = "клуби"

    def __str__(self):
        if self.name:
            return self.name
        elif self.egd_name:
            return self.egd_name
        else:
            return self.id
