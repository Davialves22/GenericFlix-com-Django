from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, FormView

from usuario.forms import CriarContaForm


# Create your views here.

class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"


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
