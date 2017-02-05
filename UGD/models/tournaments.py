from django.db import models
from .clubs import City


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
