# URL filha de URL-projectVP

from django.urls import path
from plans.views import contato, home, cadastro

urlpatterns = [
    path('', home), # Home
    path('cadastro/', cadastro), # /Sobre/
    path('contato/', contato), # /Contato/
]