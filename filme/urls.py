#url
#view - o que vai acontecer quando a pessoa clicar naquele link
#template - a parte visual que sera exibida

from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilme

#from .views import homepage, homefilmes

app_name = 'filme'

#definindo url
urlpatterns = [

    path('', Homepage.as_view(), name='homepage'),

    #filmes
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'), #pk -> primary key
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisaserie'),  # pk -> primary key

    #path('', homepage), #HomePage do site
    #path('filmes/', homefilmes),  # HomePage do site
]
