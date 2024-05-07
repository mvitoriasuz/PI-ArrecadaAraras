from django.shortcuts import render
from .models import cadastromodel
from .forms import cadastroform

app_name = 'core'

def cadastro_home(request):
    form = {'form_cadastro':cadastroform()}
    return render(request, 'Cadastro.html', form)

def cadastro(request):
    if request.method == 'post':
        form_cadastro = cadastroform(request.POST)
        if form_cadastro.is_valid():
            cad = cadastromodel.objects.create(**form_cadastro.cleaned_data)
            return render(request, "home.html")
        return render(request, 'home.html')
    else:
        contexto = {'form_cadastro': form_cadastro}
        return render(request, "Cadastro.html", contexto)

def home(request):
    contexto = {'form_cadastro': cadastroform()}
    return render(request, 'home.html', contexto)