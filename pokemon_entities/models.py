from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название покемона'
    )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Название покемона(англ.)"
        )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Название покемона(яп.)"
        )
    photo = models.ImageField(
        upload_to='media',
        blank=True,
        verbose_name='Фото покемона'
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание покемона"
    )
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="next_evolutions",
        verbose_name="Эволюция покемона",
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name="Покемон",
        related_name='entities'
    )
    appeared_at = models.DateTimeField(
        null=True,
        verbose_name="Время появления"
    )
    disappeared_at = models.DateTimeField(
        null=True,
        verbose_name="Время исчезновения"
    )
    level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Уровень покемона"
    )
    health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Здоровье покемона"
        )
    attack = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Сила атаки покемона"
    )
    protection = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Уровень зашиты покемона"
    )
    endurance = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Выносливость покемона"
    )