from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    # text = models.TextField()
    title = models.CharField(max_length=200, verbose_name="Название покемона")

    def __str__(self):
        return self.title