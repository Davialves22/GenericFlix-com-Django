from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    # (armazenar_no_bd, aparecer_pra_o_usuario),
    ("TERROR", "Terror"),
    ("SUSPENSE", "Suspense"),
    ("COMEDIA", "Comédia"),
    ("ROMANCE", "Romance"),
    ("ACAO", "Ação"),
    ("AVENTURA", "Aventura"),
    ("FICCAO_CIENTIFICA", "Ficção Científica"),
    ("FANTASIA", "Fantasia"),
    ("DRAMA", "Drama"),
    ("MISTERIO", "Mistério"),
    ("ANIMACAO", "Animação"),
    ("ANIME", "Anime"),
    ("DOCUMENTARIO", "Documentário"),
    ("BIOGRAFIA", "Biografia"),
    ("MUSICAL", "Musical"),
    ("GUERRA", "Guerra"),
    ("CRIME", "Crime"),
    ("FAMILIA", "Família"),
    ("HISTORIA", "História"),
    ("FAROESTE", "Faroeste"),
    ("OUTROS", "Outros"),
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=256)  # Campo de texto;
    thumb = models.ImageField(upload_to='thumb_filmes')  # campo de imagem;
    descricao = models.TextField(max_length=1000)  # Bloco de texto
    categoria = models.CharField(max_length=100, choices=LISTA_CATEGORIAS)
    video = models.URLField(blank=True, null=True)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)


# função padrão para formato de string
    def __str__(self):  # vai retornar uma instancia da classe filme do proprio filme
      return self.titulo

# criar o usuario
