from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"

class Criarconta( TemplateView):
        template_name = "criarconta.html"