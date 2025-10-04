from .models import Filme

#função para filmes recentes e filme em destaque
def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]
    filme_destaque = lista_filmes[0]
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}

#função para filtrar por objetos em alta
def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]#vai ordenar por ordem crescente
    return {"lista_filmes_emalta": lista_filmes}