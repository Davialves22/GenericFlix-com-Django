from django.shortcuts import render
from .models import Serie
from django.views.generic import TemplateView, ListView, DetailView

#=========================================================================#
#class base view
class Homepage(TemplateView): #vai mostrar a view
    template_name = 'homepage.html'

#series
class Homeserie(ListView):
        template_name = "homeseries.html"
        model = Serie #-> object_list -> lista de itens do modelo

class Detalhesserie(DetailView):
        template_name = "detalhesserie.html"
        model = Serie # -> 1 item do modelo

#=========================================================================#
# Create your views here.
#função da homepage
#def homepage(request): #requisição get para a homepage
#return render(request, "homepage.html")

#url -view -html
#cria uma lista de filmes da minha tabela do banco de dados
#def homefilmes(request):
#context = {}
#lista_filmes = Filme.objects.all() #pega todos os filmes do bd
#context['lista_filmes'] = lista_filmes
#return render(request, "homefilmes.html", context)

#criando uma classe para cada view
