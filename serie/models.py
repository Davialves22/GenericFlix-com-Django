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


# criar as series
class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_series")
    descricao = models.TextField(max_length=500)
    categoria = models.CharField(max_length=100, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    # função padrão para formato de string
    def __str__(self):  # vai retornar uma instancia da classe filme do proprio filme
        return self.titulo


# criar os episodios
class Episodio(models.Model):
    serie = models.ForeignKey("Serie", related_name="episodios", on_delete=models.CASCADE)  # chave estrangeira de filme
    titulo = models.CharField(max_length=256)
    video = models.URLField()

    def __str__(self):
        return self.serie.titulo + " - " + self.titulo
