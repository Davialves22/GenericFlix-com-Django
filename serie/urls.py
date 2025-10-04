# url
# view - o que vai acontecer quando a pessoa clicar naquele link
# template - a parte visual que sera exibida

from django.urls import path, include
from .views import Homepage, Detalhesserie, Homeserie, Pesquisaserie

# from .views import homepage, homefilmes

app_name = 'serie'

# definindo url
urlpatterns = [

    # series
    path('', Homeserie.as_view(), name='homeseries'),
    path('<int:pk>/', Detalhesserie.as_view(), name='detalhesserie'),  # pk -> primary key
    path('pesquisa/', Pesquisaserie.as_view(), name='pesquisaserie'),  # pk -> primary key

    # path('', homepage), #HomePage do site
    # path('filmes/', homefilmes),  # HomePage do site
]
