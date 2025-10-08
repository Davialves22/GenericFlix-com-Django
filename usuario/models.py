from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('filme.Filme', blank=True)
    series_vistas = models.ManyToManyField('serie.Serie', blank=True)
