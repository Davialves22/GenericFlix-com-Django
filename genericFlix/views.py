# [SeuAppPrincipal]/views.py

from django.views.generic import ListView
from django.db.models import Q

# IMPORTANTE: Importe os modelos de seus respectivos apps
# Certifique-se de que os nomes dos apps ('serie' e 'filme') estão corretos.
from serie.models import Serie
from filme.models import Filme


class PesquisaUnificada(ListView):
    template_name = "pesquisa.html"
    model = None
    context_object_name = 'resultados'  # Nome da variável no template

    def get_queryset(self):
        # A view espera o parâmetro 'q'
        query = self.request.GET.get('q')

        resultados_finais = []

        if query:
            # Filtro para buscar no campo 'titulo' (case-insensitive contains)
            filtro = Q(titulo__icontains=query)

            # 1. Busca em Séries
            resultados_series = Serie.objects.filter(filtro)
            resultados_finais.extend(list(resultados_series))

            # 2. Busca em Filmes
            resultados_filmes = Filme.objects.filter(filtro)
            resultados_finais.extend(list(resultados_filmes))

        return resultados_finais

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['termo_pesquisa'] = self.request.GET.get('q', '')
        return context