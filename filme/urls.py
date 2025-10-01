#url
#view - o que vai acontecer quando a pessoa clicar naquele link
#template - a parte visual que sera exibida

from django.urls import path, include
from .views import Homepage,Homefilmes
#from .views import homepage, homefilmes

#definindo url
urlpatterns = [

    path('', Homepage.as_view()),
    path('filmes/', Homefilmes.as_view()),

    #path('', homepage), #HomePage do site
    #path('filmes/', homefilmes),  # HomePage do site
] 
