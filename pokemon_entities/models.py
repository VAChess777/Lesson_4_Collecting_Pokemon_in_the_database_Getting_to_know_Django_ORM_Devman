import pathlib
from pathlib import Path

from django.db import models  # noqa F401
from django.utils import timezone

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    photo = models.ImageField(upload_to='media', blank=True, verbose_name="Фото покемона")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name="Покемон",
        related_name='entities'
    )
    appeared_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время появления"
    )
    disappeared_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время исчезновения"
    )