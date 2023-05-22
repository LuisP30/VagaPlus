from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def contato(request):
    return HttpResponse('Contato 2')

def sobre(request):
    return HttpResponse('Sobre 3')