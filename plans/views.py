from django.shortcuts import render
from django.http import HttpResponse

# Foi criada uma pasta chamada plans dentro de templates do app plans.
# A intenção é criar um namespace para o arquivo index.html para evitar colisão de arquivos com o mesmo nome.

# Foi criado um caminho > base_templates/global em VagaPlus, onde os arquivos HTML foram movidos para esse local.

def home(request):
    return render(request, 'global/index.html')

def contato(request):
    return HttpResponse('Contato')

def cadastro(request):
    return render(request,'global/sign-up.html')