from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

#=========================================================================#
#class base view
class Homepage(TemplateView): #vai mostrar a view
    template_name = 'homepage.html'

#filmes
class Homefilmes(ListView):
        template_name = "homefilmes.html"
        model = Filme #-> object_list -> lista de itens do modelo

class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme # -> 1 item do modelo

    # função que ira filtrar meus filmes por categoria e relacionar
    def get_context_data(self, **kwargs):  # parametros para passar para a função,
        context = super(Detalhesfilme, self).get_context_data(**kwargs)  # classe onde ela vai herdar tudo da classe pai
        # filtrar a tabela por series relacionadas por categoria (object)
        # self.get_object() função que vai retornar a variavel object
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]  # caso queira controlar os filmes relacionadas, pode usar [0:3]
        context['filmes_relacionados'] = filmes_relacionados
        return context


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
