from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView

#=========================================================================#
#class base view
class Homepage(TemplateView): #vai mostrar a view
    template_name = 'homepage.html'

class Homefilmes(ListView):
        template_name = "homefilmes.html"
        model = Filme #-> object_list


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
