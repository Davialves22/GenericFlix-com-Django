from .models import Serie

#função para filtrar por objetos recentes
def lista_series_recentes(request):
    lista_series = Serie.objects.all().order_by('-data_criacao')[0:10]#vai ordenar por ordem crescente
    return {"lista_series_recentes": lista_series}

#função para filtrar por objetos em alta
def lista_series_emalta(request):
    lista_series = Serie.objects.all().order_by('-visualizacoes')[0:10]#vai ordenar por ordem de visualizações
    return {"lista_series_emalta": lista_series}