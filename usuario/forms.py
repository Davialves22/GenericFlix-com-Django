from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from usuario.models import Usuario


# criando o formulario de usuario padrao e personalizado
class CriarContaForm(UserCreationForm):
    email = forms.EmailField() #campo de email obrigatorio

    #criação padrao
    class Meta:
        model = Usuario

        #campos exibidos no formulario
        fields = ('username', 'email', 'password1', 'password2')
