import pathlib
from pathlib import Path

from django.db import models  # noqa F401
from django.utils import timezone

# your models here
class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Pokemon Name'
    )
    photo = models.ImageField(
        upload_to='media',
        blank=True,
        verbose_name='Pokemon Photo'
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание покемона"
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(
        verbose_name='Latitude'
    )
    longitude = models.FloatField(
        verbose_name='Longitude'
    )
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name="Pokemon",
        related_name='entities'
    )
    appeared_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Time of appearance"
    )
    disappeared_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Time of disappearance"
    )
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Level"
    )
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Health"
        )
    attack = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Attack"
    )
    protection = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Protection"
    )
    endurance = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Endurance"
    )