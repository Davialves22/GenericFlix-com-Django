from filme.models import Filme
from .models import Serie


# função para filtrar por objetos recentes
def lista_series_recentes(request):
    lista_series = Serie.objects.all().order_by('-data_criacao')[0:8]  # vai ordenar por ordem crescente
    if lista_series:
        serie_destaque = lista_series[0]
    else:
        serie_destaque = None
    return {"lista_series_recentes": lista_series, "serie_destaque": serie_destaque}


# função para filtrar por objetos em alta
def lista_series_emalta(request):
    lista_series = Serie.objects.all().order_by('-visualizacoes')[0:8]  # vai ordenar por ordem de visualizações
    return {"lista_series_emalta": lista_series}
