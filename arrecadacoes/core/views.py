from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

from .forms import CadastroForm

def index(request):
    return render(request, 'index.html')

def cadastro_view(request):
    if request.method == 'POST':
        form_cadastro = CadastroForm(request.POST)
        if form_cadastro.is_valid():
            instance = form_cadastro.save()
            print("Registro salvo com sucesso:", instance)
            return redirect('core:index')
    else:
        form_cadastro = CadastroForm()

    contexto = {'form_cadastro': form_cadastro}
    return render(request, "cadastro.html", contexto)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', reverse('core:index')))
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def ongs_view(request):
    return render(request, 'ongs.html')
