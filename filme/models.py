from django.db import models
from django.utils import timezone


# Create your models here.

LISTA_CATEGORIAS = (
    # (armazenar_no_bd, aparecer_pra_o_usuario),
    ("TERROR", "Terror"),
    ("SUSPENSE", "Suspense"),
    ("COMEDIA", "Comédia"),
    ("OUTROS", "Outros"),
)


# criar o filme
class Filme(models.Model):
    tituto = models.CharField(max_length=256)  # Campo de texto;
    thumb = models.ImageField(upload_to='thumb_filmes') #campo de imagem;
    descricao = models.TextField(max_length=1000)  # Bloco de texto
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0) 
    data_criacao = models.DateTimeField(default=timezone.now)

# criar os episodios

# criar o usuario
