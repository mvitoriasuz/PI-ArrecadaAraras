from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.exceptions import ValidationError
from .forms import CadastroForm
from .services import CadastroClienteService
from .services import LogarUsuarioService
from django.contrib.auth.decorators import login_required
from .forms import DoacaoForm
from .forms import LoginForm
from django.shortcuts import redirect


def index(request):
    return render(request, "index.html")


def cadastro_view(request):
    if request.method == "POST":
        form_cadastro = CadastroForm(request.POST)
        if form_cadastro.is_valid():
            try:
                service = CadastroClienteService()
                resultado = service.cadastrar_cliente(
                    nome=form_cadastro.cleaned_data["nome"],
                    cpf=form_cadastro.cleaned_data["cpf"],
                    email=form_cadastro.cleaned_data["email"],
                    senha=form_cadastro.cleaned_data["senha"],
                    data_nasc=form_cadastro.cleaned_data["data_nasc"],
                )
                if "error" in resultado:
                    form_cadastro.add_error(None, resultado["error"])
                else:
                    return redirect("core:index")
            except ValidationError as e:
                form_cadastro.add_error(None, e.message)
    else:
        form_cadastro = CadastroForm()

    contexto = {"form_cadastro": form_cadastro}
    return render(request, "cadastro.html", contexto)


from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('core:index'))
            else:
                return render(request, "login.html", {"form": form, "error_message": "Credenciais inválidas."})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('core:index')


def ongs_view(request):
    return render(request, "ongs.html")


@login_required
def doacao_view(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            cliente_id = request.user.id
            ong_id = form.cleaned_data['ong_id']
            descricao_doacao = form.cleaned_data['descricao_doacao']
            logar_service = LogarUsuarioService()
            resultado = logar_service.fazer_doacao(cliente_id, ong_id, descricao_doacao)
            if 'success' in resultado:
                return redirect(reverse('core:index'))
            else:
                return render(request, 'doacao.html', {'form': form, 'error_message': resultado['error']})
    else:
        form = DoacaoForm()

    return render(request, 'doacao.html', {'form': form})