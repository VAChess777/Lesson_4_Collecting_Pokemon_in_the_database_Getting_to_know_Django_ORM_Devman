from django.contrib import admin
# Register your models here.
from .models import Pokemon
from .models import PokemonEntity

admin.site.register(Pokemon)
admin.site.register(PokemonEntity)