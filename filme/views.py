from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from usuario.models import Usuario


# =========================================================================#
# class base view
class Homepage(TemplateView):  # vai mostrar a view
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # usuario esta autenticado
            # redireciona pra home
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)  # redireciona para a homepage


# filmes
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme  # -> object_list -> lista de itens do modelo


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme  # -> 1 item do modelo

    # função para contabilizar a visualização
    def get(self, request, *args, **kwargs):
        # descobrir qual serie o usuario ta acessando
        filme = self.get_object()
        # somar 1 nas visualizacoes daquela serie
        filme.visualizacoes += 1
        # salvar
        filme.save()

        usuario = request.user
        usuario.filmes_vistos.add(filme)

        return super().get(request, *args, **kwargs)  # redireciona o usuario para a url final

    # função que ira filtrar meus filmes por categoria e relacionar
    def get_context_data(self, **kwargs):  # parametros para passar para a função,
        context = super(Detalhesfilme, self).get_context_data(**kwargs)  # classe onde ela vai herdar tudo da classe pai
        # filtrar a tabela por series relacionadas por categoria (object)
        # self.get_object() função que vai retornar a variavel object
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[
            0:5]  # caso queira controlar os filmes relacionadas, pode usar [0:3]
        context['filmes_relacionados'] = filmes_relacionados
        return context
    # Função para a barra de pesquisa


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme  # -> object_list -> lista de itens do modelo

# =========================================================================#
# Create your views here.
# função da homepage
# def homepage(request): #requisição get para a homepage
# return render(request, "homepage.html")

# url -view -html
# cria uma lista de filmes da minha tabela do banco de dados
# def homefilmes(request):
# context = {}
# lista_filmes = Filme.objects.all() #pega todos os filmes do bd
# context['lista_filmes'] = lista_filmes
# return render(request, "homefilmes.html", context)

# criando uma classe para cada view
