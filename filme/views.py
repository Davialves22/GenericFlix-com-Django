from django.shortcuts import render
from .models import Filme

from filme.models import Filme


# Create your views here.

#função da homepage
def homepage(request): #requisição get para a homepage
  return render(request, "homepage.html")

#url -view -html
#cria uma lista de filmes da minha tabela do banco de dados
def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all() #pega todos os filmes do bd
    context['lista_filmes'] = lista_filmes
    return render(request, "homefilmes.html", context)