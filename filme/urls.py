#url
#view - o que vai acontecer quando a pessoa clicar naquele link
#template - a parte visual que sera exibida

from django.urls import path, include
from .views import homepage

#definindo url
urlpatterns = [
    path('', homepage), #HomePage do site
] 
