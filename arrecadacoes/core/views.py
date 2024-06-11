from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.core.exceptions import ValidationError
from .forms import CadastroForm
from .services import CadastroClienteService
from django.contrib.auth.decorators import login_required
from .models import Doacao
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def cadastro_view(request):
    if request.method == 'POST':
        form_cadastro = CadastroForm(request.POST)
        if form_cadastro.is_valid():
            try:
                service = CadastroClienteService()
                resultado = service.cadastrar_cliente(
                    nome=form_cadastro.cleaned_data['nome'],
                    cpf=form_cadastro.cleaned_data['cpf'],
                    email=form_cadastro.cleaned_data['email'],
                    senha=form_cadastro.cleaned_data['senha'],
                    data_nasc=form_cadastro.cleaned_data['data_nasc']
                )
                if 'error' in resultado:
                    form_cadastro.add_error(None, resultado['error'])
                else:
                    return redirect('core:index')
            except ValidationError as e:
                form_cadastro.add_error(None, e.message)
    else:
        form_cadastro = CadastroForm()

    contexto = {'form_cadastro': form_cadastro}
    return render(request, "cadastro.html", contexto)

def login_view(request):
    if request.method == 'POST':
        print("Formulário de login submetido!")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("Dados do formulário são válidos!")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Usuário autenticado com sucesso!")
                login(request, user)
                return redirect(reverse('core:index'))  # Redireciona para a página inicial após o login
            else:
                print("Usuário não autenticado. Credenciais inválidas.")
                # Lida com credenciais inválidas
                return render(request, 'login.html', {'form': form, 'error_message': 'Credenciais inválidas.'})
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



def ongs_view(request):
    return render(request, 'ongs.html')

@login_required
def fazer_doacao(request):
    if request.method == 'POST':
        ong_nome = request.POST.get('ong_nome')
        item_doado = request.POST.get('item_doado')
        quantidade_doada = request.POST.get('quantidade_doada')

        # Obtém o usuário autenticado
        user = request.user  

        # Cria a doação associada ao usuário autenticado
        doacao = Doacao.objects.create(
            user=user,  # Associa a doação ao usuário autenticado
            ong_nome=ong_nome,
            item_doado=item_doado,
            quantidade_doada=quantidade_doada
        )
        
        messages.success(request, 'Doação registrada com sucesso!')
        return redirect('perfil_usuario')
    else:
        messages.error(request, 'Erro ao processar a doação. Tente novamente.')
        return redirect('pagina_anterior')