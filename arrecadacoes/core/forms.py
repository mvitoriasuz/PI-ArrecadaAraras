from django import forms
from.models import CadastroModel  # Corrigindo o nome do modelo para seguir a convenção de nomes em Python
from django.core.exceptions import ValidationError
import re

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

    def clean_nome_completo(self):
        nome = self.cleaned_data['nome']
        palavras = [w.capitalize() for w in nome.split()]
        return ' '.join(palavras)

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not cpf.isdigit() or len(cpf)!= 11:
            raise ValidationError('CPF deve conter apenas onze dígitos.')
        return cpf

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(re.findall(r"@", email))!= 1 or len(re.findall(r"\.", email)) == 0:
            raise ValidationError('Por favor, insira um email válido.')
        return email

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$%*?&])[A-Za-z\d@$%*?&]{10,}$"
        if not re.match(pattern, senha):
            raise ValidationError('Sua senha deve ter pelo menos 10 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.')
        return senha


    def clean_data_nasc(self):
        data_nasc = self.cleaned_data['data_nasc']
        return data_nasc
