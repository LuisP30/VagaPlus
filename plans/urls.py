from django.urls import path
from plans.views import contato, home, sobre 

urlpatterns = [
    path('', home), # Home
    path('sobre/', sobre), # /sobre/
    path('contato/', contato), # /contato/
]