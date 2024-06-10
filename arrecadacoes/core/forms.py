from django import forms
from django.core.exceptions import ValidationError
from .models import CadastroModel
from .services import CadastroClienteService
import re
from datetime import datetime

class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroModel
        fields = ['nome', 'cpf', 'email', 'senha', 'data_nasc']
        widgets = {
            'senha': forms.PasswordInput(),
        }
        error_messages = {
            'nome': {'required': "Erro ao informar o campo nome."},
            'cpf': {'required': "Erro ao informar o campo cpf."},
            'email': {'required': "Erro ao informar o campo email."},
            'senha': {'required': "Erro ao informar o campo senha."},
            'data_nasc': {'required': "Erro ao informar o campo data_nasc."},
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        palavras = [w.capitalize() for w in nome.split()]
        return ' '.join(palavras)

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError('CPF deve conter apenas onze dígitos.')
        return cpf

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(re.findall(r"@", email)) != 1 or len(re.findall(r"\.", email)) == 0:
            raise ValidationError('Por favor, insira um email válido.')
        return email

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 10:
            raise ValidationError('Sua senha deve ter pelo menos 10 caracteres.')
        return senha


    def clean_data_nasc(self):
        data_nasc = self.cleaned_data['data_nasc']
        if isinstance(data_nasc, datetime):
            data_nasc = data_nasc.date()
        data_nasc_str = data_nasc.strftime('%Y-%m-%d')
        return data_nasc_str

    def registrar_cliente(self, commit=True):
        data = self.cleaned_data
        cadastro_service = CadastroClienteService()
        resultado = cadastro_service.cadastrar_cliente(
            nome=data['nome'],
            cpf=data['cpf'],
            email=data['email'],
            senha=data['senha'],
            data_nasc=data['data_nasc']
        )
        if 'error' in resultado:
            raise ValidationError(resultado['error'])
        return resultado
