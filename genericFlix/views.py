# [SeuAppPrincipal]/views.py

from django.views.generic import ListView
from django.db.models import Q
from serie.models import Serie
from filme.models import Filme


class PesquisaUnificada(ListView):
    template_name = "pesquisa.html"
    model = None
    context_object_name = 'resultados'

    def get_queryset(self):
        query = self.request.GET.get('q')
        resultados_finais = []

        # 1. TRATAMENTO PARA BUSCA VAZIA (NOVO CÓDIGO AQUI)
        if not query:
            # Se a busca estiver vazia (ou for a primeira visita sem termo)
            # Retorna TODOS os filmes e séries
            resultados_finais.extend(list(Serie.objects.all()))
            resultados_finais.extend(list(Filme.objects.all()))


        # 2. LÓGICA DE PESQUISA NORMAL (SE HOUVER UM TERMO)
        else:
            # Se houver um termo, faz a busca filtrada
            filtro = Q(titulo__icontains=query)

            resultados_series = Serie.objects.filter(filtro)
            resultados_finais.extend(list(resultados_series))

            resultados_filmes = Filme.objects.filter(filtro)
            resultados_finais.extend(list(resultados_filmes))

        # Retorna a lista combinada (todos, ou filtrados)
        return resultados_finais

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # O termo de pesquisa pode ser vazio.
        context['termo_pesquisa'] = self.request.GET.get('q', '')
        return context