# url
# view - o que vai acontecer quando a pessoa clicar naquele link
# template - a parte visual que sera exibida

from django.urls import path, include
from django.contrib.auth import views as auth_view

from usuario.views import Paginaperfil,Criarconta


app_name = 'usuario'

# definindo url
urlpatterns = [

    # usuarios
    path('login/', auth_view.LoginView.as_view(template_name = "login.html"), name='login'),  # pk -> primary key
    path('logout/', auth_view.LogoutView.as_view(template_name = "logout.html"), name='logout'),  # pk -> primary key
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),  # pk -> primary key
    path('criarconta/', Criarconta.as_view(), name='criarconta'),  # pk -> primary key

    # path('', homepage), #HomePage do site
    # path('filmes/', homefilmes),  # HomePage do site
]
