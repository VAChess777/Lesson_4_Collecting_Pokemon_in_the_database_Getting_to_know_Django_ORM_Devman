import pathlib
from pathlib import Path

from django.db import models  # noqa F401
from django.utils import timezone

# your models here
class Pokemon(models.Model):
    # text = models.TextField()
    title = models.CharField(max_length=200, verbose_name="Название покемона")

    photo = models.ImageField(upload_to='media',
                              blank=True,
                              verbose_name="Фото покемона"
                              )

    def __str__(self):
        return self.title