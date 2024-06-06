from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from.models import CadastroModel
from.forms import CadastroForm
# from.forms import LoginForm

app_name = 'core'

def index(request):
    return render(request, 'index.html')


def cadastro_view(request):
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


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Substitua 'home' pela URL onde você deseja redirecionar após o login
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


