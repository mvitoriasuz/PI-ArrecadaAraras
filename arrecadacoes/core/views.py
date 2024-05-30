from django.shortcuts import render, redirect
from.models import CadastroModel
from.forms import CadastroForm

app_name = 'core'

def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        form_cadastro = CadastroForm(request.POST)
        if form_cadastro.is_valid(): 
            cad = CadastroModel.objects.create(**form_cadastro.cleaned_data)
            # Redireciona para a página inicial após o cadastro bem-sucedido
            return redirect('index')  
    else:
        form_cadastro = CadastroForm()

    contexto = {'form_cadastro': form_cadastro}
    return render(request, "Cadastro.html", contexto)


