from django import forms
from .models import cadastromodel
from django.core.exceptions import ValidationError
import re

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números')
    if len(value) != 11:
        raise ValidationError('CPF deve conter onze números')
    
def validate_email(email):
    if len(re.findall(r"@", email)) != 1 or len(re.findall(r"\.", email)) >= 1:
        raise forms.ValidationError('por favor inserir um email valido')
    

def validate_senha(password):
    minimal_number = 2
    minimal_upper_char = 2
    minimal_lower_char = 2
    minimal_special_char = 1
    minimal_len_char = 10
    if len(password or ()) < minimal_len_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_len_char)+' caracteres')
    if len(re.findall(r"[A-Z]", password)) < minimal_upper_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_upper_char)+' letras maiusculas')
    if len(re.findall(r"[a-z]", password)) < minimal_lower_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_lower_char)+' letras minusculas')
    if len(re.findall(r"[0-9]", password)) < minimal_number:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_number)+' numeros')
    if len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><\.]", password)) < minimal_special_char:
        raise forms.ValidationError('Senha tem que ter no mínimo '+str(minimal_special_char)+' caracteres especiais')

class cadastroform(forms.ModelForm):
    class meta:
        model = cadastromodel
        fields = ['nome', 'cpf ','email', 'senha', 'data_nasc' ]
        error_messages = {
            'nome': {
                'required': ("Erro ao informar o campo nome."),
            },
            'cpf': {
                'required': ("Erro ao informar o campo cpf."),
            },
            'email': {
                'required': ("Erro ao informar o campo email."),
            },
            'senha': {
                'required': ("Erro ao informar o campo senha."),
            },
            'data_nasc': {
                'required': ("Erro ao informar o campo data_nasc."),
            },
        }

        def clean_nome_completo(self):
            nome = self.cleaned_data['nome']
            palavras = [w.capitalize() for w in nome.split()]
            return ' '.join(palavras)

        def clean_cpf(self):
            cpf = self.cleaned_data['cpf']
            validate_cpf(cpf)
            return cpf
        
        def clean_email(self):
            email = self.cleaned_data['email']
            validate_email(email)
            return email
        
        def clean_senha(self):
            senha = self.cleaned_data['senha']
            validate_senha(senha)
            return senha
        
        def clean_data_nasc(self):
            data_nasc = self.cleaned_data_nasc['data_nasc']
            return data_nasc
        
        def clean(self):
            self.cleaned_data = super().clean()
            return self.cleaned_data
        