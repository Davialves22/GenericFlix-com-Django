from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, FormView, UpdateView

from usuario.forms import CriarContaForm
from usuario.models import Usuario


# Create your views here.

# view para atualização de dados
class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('homefilmes')


# view com o formulario form
class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    # vai criar o usuario e salvar no bd
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # caso o form seja feito com sucesso ira redirecionar
    def get_success_url(self):
        return reverse('usuario:login')  # reverse se usa quando uma função pede um texto de link com essa
